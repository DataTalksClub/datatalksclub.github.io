#!/usr/bin/env python3
"""
Add duration field to podcast files based on transcript start and end times.

This script calculates the duration from the transcript's first and last timestamp
and adds a 'duration' field to the frontmatter in ISO 8601 format (e.g., PT00H30M5S).

Usage:
    python add_duration_from_transcript.py <podcast_file1> <podcast_file2> ...
    python add_duration_from_transcript.py --all-in-dir _podcast/
    python add_duration_from_transcript.py --all

Options:
    --all-in-dir DIR  Process all .md files in the specified directory
    --all             Process all podcast files in _podcast/
    --dry-run         Show what would be done without updating files
    --force           Overwrite existing duration field if it exists
"""

import argparse
import re
import sys
import yaml
from pathlib import Path
from typing import List, Optional, Tuple


def get_project_root() -> Path:
    """Return the project root directory (parent of scripts directory)."""
    return Path(__file__).parent.parent


def resolve_podcast_path(podcast_file: str) -> Optional[Path]:
    """Resolve a podcast file path relative to the project root."""
    project_root = get_project_root()
    file_path = Path(podcast_file)

    if file_path.exists():
        return file_path.resolve()

    candidate = project_root / podcast_file
    if candidate.exists():
        return candidate.resolve()

    return None


def calculate_duration_from_transcript(transcript: List) -> Optional[str]:
    """
    Calculate duration from transcript by finding first and last sec values.
    
    Args:
        transcript: List of transcript items (dicts with 'sec', 'time', 'line', etc.)
    
    Returns:
        ISO 8601 duration string (e.g., "PT00H30M5S") or None if cannot calculate
    """
    start_sec = None
    end_sec = None
    
    for item in transcript:
        if isinstance(item, dict) and 'sec' in item:
            sec_value = item['sec']
            if isinstance(sec_value, (int, float, str)):
                try:
                    sec_int = int(float(sec_value))
                    if start_sec is None:
                        start_sec = sec_int
                    end_sec = sec_int
                except (ValueError, TypeError):
                    continue
    
    if start_sec is None or end_sec is None:
        return None
    
    # Calculate duration in seconds
    duration_seconds = end_sec - start_sec
    
    if duration_seconds < 0:
        return None
    
    # Convert to ISO 8601 format (PT00H30M5S)
    hours = duration_seconds // 3600
    minutes = (duration_seconds % 3600) // 60
    seconds = duration_seconds % 60
    
    # Format as PT00H30M5S (always include hours, even if zero)
    duration_parts = ["PT", f"{hours:02d}H"]
    if minutes > 0:
        duration_parts.append(f"{minutes:02d}M")
    if seconds > 0 or (hours == 0 and minutes == 0):
        duration_parts.append(f"{seconds:02d}S")
    
    return "".join(duration_parts)


def add_duration_to_file(file_path: Path, force: bool = False, dry_run: bool = False) -> bool:
    """
    Add duration field to a podcast file's frontmatter.
    
    Args:
        file_path: Path to the podcast markdown file
        force: If True, overwrite existing duration field
        dry_run: If True, don't actually modify the file
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ Error reading file: {e}", file=sys.stderr)
        return False

    # Find the frontmatter section
    if not content.startswith('---\n'):
        print(f"  ✗ File does not start with frontmatter delimiter", file=sys.stderr)
        return False
    
    # Find the closing --- (try both \n---\n and \n---)
    match = re.search(r'\n---\n', content[4:])
    has_trailing_newline = True
    if not match:
        # Try without trailing newline
        match = re.search(r'\n---', content[4:])
        has_trailing_newline = False
    
    if not match:
        print(f"  ✗ Could not find closing frontmatter delimiter", file=sys.stderr)
        return False
    
    # match.start() is relative to content[4:], so add 4 to get absolute position
    # The match starts at the \n before ---, so add 1 to get to the start of ---
    frontmatter_end = match.start() + 4 + 1  # Position of first '-' in closing ---
    frontmatter_text = content[4:frontmatter_end]
    
    # Extract rest of content after closing ---
    if has_trailing_newline:
        # Format: \n---\n, so skip ---\n (4 chars)
        rest_content = content[frontmatter_end + 4:]
    else:
        # Format: \n---, so skip --- (3 chars)
        rest_content = content[frontmatter_end + 3:]
    
    # Parse frontmatter
    try:
        frontmatter_data = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as e:
        print(f"  ✗ Failed to parse YAML frontmatter: {e}", file=sys.stderr)
        return False
    
    if frontmatter_data is None:
        frontmatter_data = {}
    
    # Check if duration already exists
    if 'duration' in frontmatter_data and not force:
        print(f"  ⊘ Skipping (duration already exists: {frontmatter_data['duration']})")
        return True

    # Get transcript from frontmatter
    transcript = frontmatter_data.get('transcript', [])
    if not transcript:
        print(f"  ⊘ Skipping (no transcript found)")
        return True

    # Calculate duration from transcript
    duration = calculate_duration_from_transcript(transcript)
    if not duration:
        print(f"  ✗ Could not calculate duration from transcript")
        return False

    # Add or update duration field
    frontmatter_data['duration'] = duration

    if dry_run:
        print(f"  [DRY RUN] Would add duration: {duration}")
        return True

    # Convert back to YAML
    try:
        new_frontmatter = yaml.dump(frontmatter_data, default_flow_style=False, allow_unicode=True, sort_keys=False)
    except Exception as e:
        print(f"  ✗ Failed to serialize YAML: {e}", file=sys.stderr)
        return False
    
    # Ensure frontmatter ends with newline before closing ---
    if not new_frontmatter.endswith('\n'):
        new_frontmatter += '\n'
    
    # Reconstruct file
    new_content = f"---\n{new_frontmatter}---\n{rest_content}"

    # Write the file back
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✓ Added duration: {duration}")
        return True
    except Exception as e:
        print(f"  ✗ Error writing file: {e}", file=sys.stderr)
        return False


def get_podcast_files_from_args(args: argparse.Namespace) -> List[Path]:
    """Collect podcast files based on CLI arguments."""
    files: List[Path] = []
    project_root = get_project_root()

    if args.all:
        # Process all podcast files
        podcast_dir = project_root / '_podcast'
        if not podcast_dir.exists():
            print(f"Error: Podcast directory not found: {podcast_dir}", file=sys.stderr)
            sys.exit(1)
        files = sorted(podcast_dir.glob('*.md'))
        # Exclude template files
        files = [f for f in files if not f.name.startswith('_')]
    
    elif args.all_in_dir:
        # Get all .md files in directory
        dir_path = Path(args.all_in_dir)
        if not dir_path.is_absolute():
            dir_path = project_root / args.all_in_dir
        
        if not dir_path.exists():
            print(f"Error: Directory not found: {args.all_in_dir}", file=sys.stderr)
            sys.exit(1)
        
        files = sorted(dir_path.glob('*.md'))
    
    else:
        # From command line arguments
        for podcast_file in args.podcast_files:
            file_path = resolve_podcast_path(podcast_file)
            if file_path:
                files.append(file_path)
            else:
                print(f"Error: File not found: {podcast_file}", file=sys.stderr)
                sys.exit(1)
    
    return files


def main():
    parser = argparse.ArgumentParser(
        description='Add duration field to podcast files based on transcript timestamps',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process specific files
  python add_duration_from_transcript.py _podcast/s01e01-roles.md _podcast/s01e02-processes.md
  
  # Process all files in a directory
  python add_duration_from_transcript.py --all-in-dir _podcast/
  
  # Process all podcast files
  python add_duration_from_transcript.py --all
  
  # Dry run to see what would be done
  python add_duration_from_transcript.py --all --dry-run
  
  # Force overwrite existing duration fields
  python add_duration_from_transcript.py --all --force
        """
    )
    
    parser.add_argument(
        'podcast_files',
        nargs='*',
        help='Podcast markdown files to process'
    )
    
    parser.add_argument(
        '--all-in-dir',
        metavar='DIR',
        help='Process all .md files in the specified directory'
    )
    
    parser.add_argument(
        '--all',
        action='store_true',
        help='Process all podcast files in _podcast/'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without updating files'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='Overwrite existing duration field if it exists'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.podcast_files and not args.all_in_dir and not args.all:
        parser.error('Must specify podcast files, --all-in-dir, or --all')
    
    # Get list of files to process
    files = get_podcast_files_from_args(args)
    
    if not files:
        print("No files to process.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing {len(files)} file(s)...")
    if args.dry_run:
        print("(DRY RUN - no files will be modified)")
    print()
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for file_path in files:
        print(f"Processing: {file_path.name}")
        
        # Check if duration exists and we're not forcing
        if not args.force:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if content.startswith('---\n'):
                    match = re.search(r'\n---(\n|$)', content[4:])
                    if match:
                        frontmatter_text = content[4:match.start() + 4]
                        frontmatter_data = yaml.safe_load(frontmatter_text)
                        if frontmatter_data and 'duration' in frontmatter_data:
                            print(f"  ⊘ Skipping (duration already exists: {frontmatter_data['duration']})")
                            skip_count += 1
                            continue
            except Exception:
                # If we can't read it, try to process it anyway
                pass
        
        if add_duration_to_file(file_path, force=args.force, dry_run=args.dry_run):
            success_count += 1
        else:
            error_count += 1
        print()
    
    # Summary
    print("=" * 60)
    print(f"Summary:")
    print(f"  Success: {success_count}")
    if skip_count > 0:
        print(f"  Skipped: {skip_count}")
    if error_count > 0:
        print(f"  Errors: {error_count}")
    print("=" * 60)


if __name__ == '__main__':
    main()

