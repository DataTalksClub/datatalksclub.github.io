#!/usr/bin/env python3
"""
Add quotable clips field to podcast files based on timestamps files.

This script reads timestamp files from podcast-timestamps/ folder and adds
a 'quotableClips' field to the frontmatter with structured clip data including:
- name: The timestamp title/description
- startOffset: Start time in seconds
- url: YouTube URL with time parameter

Usage:
    python add_quotable_clips.py <podcast_file1> <podcast_file2> ...
    python add_quotable_clips.py --all-in-dir _podcast/
    python add_quotable_clips.py --all

Options:
    --all-in-dir DIR  Process all .md files in the specified directory
    --all             Process all podcast files in _podcast/
    --dry-run         Show what would be done without updating files
    --force           Overwrite existing quotableClips field if it exists
"""

import argparse
import re
import sys
import yaml
from pathlib import Path
from typing import List, Optional, Dict, Tuple


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


def parse_timestamps_file(timestamps_file_path: Path) -> List[Tuple[int, str]]:
    """
    Parse a timestamps file and return list of (seconds, topic) tuples.
    
    Expected format: HH:MM:SS Topic text
    Example: 00:01:12 Podcasts Overview: Vanishing Gradients and High Signal
    """
    timestamps = []
    
    if not timestamps_file_path.exists():
        return timestamps
    
    try:
        with open(timestamps_file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                    
                # Match pattern: HH:MM:SS Topic
                match = re.match(r'^(\d{2}):(\d{2}):(\d{2})\s+(.+)$', line)
                if not match:
                    continue
                
                hours, minutes, seconds, topic = match.groups()
                total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
                timestamps.append((total_seconds, topic.strip()))
    except Exception as e:
        print(f"  ✗ Error reading timestamps file: {e}", file=sys.stderr)
    
    return timestamps


def get_timestamps_file_path(podcast_file_path: Path) -> Path:
    """Get the corresponding timestamps file path for a podcast file."""
    project_root = get_project_root()
    # Get the filename without extension and add .txt
    timestamps_filename = podcast_file_path.stem + '.txt'
    return project_root / 'podcast-timestamps' / timestamps_filename


def build_youtube_url(base_url: str, start_offset: int) -> str:
    """
    Build YouTube URL with time parameter.
    
    Args:
        base_url: Base YouTube URL (e.g., https://www.youtube.com/watch?v=-Gj7SaI-QW4)
        start_offset: Start time in seconds
    
    Returns:
        URL with time parameter (e.g., https://www.youtube.com/watch?v=-Gj7SaI-QW4&t=120)
    """
    # Check if URL already has query parameters
    if '?' in base_url:
        separator = '&'
    else:
        separator = '?'
    
    return f"{base_url}{separator}t={start_offset}"


def parse_duration_to_seconds(duration: str) -> Optional[int]:
    """
    Parse ISO 8601 duration string to total seconds.
    
    Args:
        duration: ISO 8601 duration (e.g., "PT00H58M11S")
    
    Returns:
        Total seconds or None if parsing fails
    """
    if not duration or not duration.startswith('PT'):
        return None
    
    # Extract hours, minutes, seconds
    hours_match = re.search(r'(\d+)H', duration)
    minutes_match = re.search(r'(\d+)M', duration)
    seconds_match = re.search(r'(\d+)S', duration)
    
    hours = int(hours_match.group(1)) if hours_match else 0
    minutes = int(minutes_match.group(1)) if minutes_match else 0
    seconds = int(seconds_match.group(1)) if seconds_match else 0
    
    return hours * 3600 + minutes * 60 + seconds


def add_endoffset_to_existing_clips(existing_clips: List[Dict], timestamps: List[Tuple[int, str]], duration: Optional[str] = None) -> List[Dict]:
    """
    Add endOffset to existing clips that are missing it.
    
    Args:
        existing_clips: List of existing clip dictionaries
        timestamps: List of (seconds, topic) tuples from timestamps file
        duration: Optional ISO 8601 duration string for calculating last clip's endOffset
    
    Returns:
        Updated list of clips with endOffset added
    """
    total_duration_seconds = None
    if duration:
        total_duration_seconds = parse_duration_to_seconds(duration)
    
    # Create a mapping from startOffset to endOffset
    offset_map = {}
    for i, (start_offset, _) in enumerate(timestamps):
        if i < len(timestamps) - 1:
            offset_map[start_offset] = timestamps[i + 1][0]
        else:
            offset_map[start_offset] = total_duration_seconds if total_duration_seconds else start_offset
    
    updated_clips = []
    for clip in existing_clips:
        if isinstance(clip, dict):
            updated_clip = clip.copy()
            if 'endOffset' not in updated_clip and 'startOffset' in updated_clip:
                start_offset = updated_clip['startOffset']
                updated_clip['endOffset'] = offset_map.get(start_offset, start_offset)
            updated_clips.append(updated_clip)
        else:
            updated_clips.append(clip)
    
    return updated_clips


def create_quotable_clips(timestamps: List[Tuple[int, str]], youtube_url: str, duration: Optional[str] = None) -> List[Dict]:
    """
    Create quotable clips list from timestamps.
    
    Args:
        timestamps: List of (seconds, topic) tuples
        youtube_url: Base YouTube URL
        duration: Optional ISO 8601 duration string for calculating last clip's endOffset
    
    Returns:
        List of clip dictionaries with name, startOffset, endOffset, and url
    """
    clips = []
    total_duration_seconds = None
    
    if duration:
        total_duration_seconds = parse_duration_to_seconds(duration)
    
    for i, (start_offset, name) in enumerate(timestamps):
        # Calculate endOffset: next clip's startOffset, or video duration for last clip
        if i < len(timestamps) - 1:
            end_offset = timestamps[i + 1][0]
        else:
            # Last clip: use duration if available, otherwise use startOffset (fallback)
            end_offset = total_duration_seconds if total_duration_seconds else start_offset
        
        clip = {
            'name': name,
            'startOffset': start_offset,
            'endOffset': end_offset,
            'url': build_youtube_url(youtube_url, start_offset)
        }
        clips.append(clip)
    
    return clips


def add_quotable_clips_to_file(file_path: Path, force: bool = False, dry_run: bool = False) -> bool:
    """
    Add quotableClips field to a podcast file's frontmatter.
    
    Args:
        file_path: Path to the podcast markdown file
        force: If True, overwrite existing quotableClips field
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
    
    # Check if quotableClips already exists
    existing_clips = frontmatter_data.get('quotableClips', [])
    has_existing_clips = bool(existing_clips)
    
    # Check if clips exist but are missing endOffset
    needs_endoffset_update = False
    if has_existing_clips and not force:
        # Check if any clip is missing endOffset
        for clip in existing_clips:
            if isinstance(clip, dict) and 'endOffset' not in clip:
                needs_endoffset_update = True
                break
        
        if not needs_endoffset_update:
            print(f"  ⊘ Skipping (quotableClips already exists with {len(existing_clips)} clips and all have endOffset)")
            return True
        else:
            print(f"  ℹ Found {len(existing_clips)} clips missing endOffset, will update them")

    # Get YouTube URL from frontmatter
    youtube_url = frontmatter_data.get('links', {}).get('youtube')
    if not youtube_url or youtube_url == 'TODO':
        print(f"  ⊘ Skipping (no YouTube URL found)")
        return True

    # Get timestamps file path
    timestamps_file = get_timestamps_file_path(file_path)
    if not timestamps_file.exists():
        print(f"  ⊘ Skipping (timestamps file not found: {timestamps_file.name})")
        return True

    # Parse timestamps
    timestamps = parse_timestamps_file(timestamps_file)
    if not timestamps:
        print(f"  ⊘ Skipping (no timestamps found in file)")
        return True

    # Get duration from frontmatter for calculating last clip's endOffset
    duration = frontmatter_data.get('duration')

    # If clips exist but are missing endOffset, update them
    if needs_endoffset_update:
        quotable_clips = add_endoffset_to_existing_clips(existing_clips, timestamps, duration)
        if dry_run:
            print(f"  [DRY RUN] Would update {len(quotable_clips)} clips with endOffset")
            if quotable_clips:
                print(f"    First clip: {quotable_clips[0]['name']} at {quotable_clips[0]['startOffset']}s, endOffset: {quotable_clips[0].get('endOffset', 'N/A')}")
                print(f"    Last clip: {quotable_clips[-1]['name']} at {quotable_clips[-1]['startOffset']}s, endOffset: {quotable_clips[-1].get('endOffset', 'N/A')}")
            return True
    else:
        # Create new quotable clips
        quotable_clips = create_quotable_clips(timestamps, youtube_url, duration)
        if dry_run:
            print(f"  [DRY RUN] Would add {len(quotable_clips)} quotable clips")
            if quotable_clips:
                print(f"    First clip: {quotable_clips[0]['name']} at {quotable_clips[0]['startOffset']}s")
                print(f"    Last clip: {quotable_clips[-1]['name']} at {quotable_clips[-1]['startOffset']}s")
            return True

    # Add or update quotableClips field
    frontmatter_data['quotableClips'] = quotable_clips

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
        if needs_endoffset_update:
            print(f"  ✓ Updated {len(quotable_clips)} clips with endOffset")
        else:
            print(f"  ✓ Added {len(quotable_clips)} quotable clips")
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
        description='Add quotableClips field to podcast files based on timestamps files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process specific files
  python add_quotable_clips.py _podcast/s14e05-lessons-learned-from-freelancing-and-working-in-start-up.md
  
  # Process all files in a directory
  python add_quotable_clips.py --all-in-dir _podcast/
  
  # Process all podcast files
  python add_quotable_clips.py --all
  
  # Dry run to see what would be done
  python add_quotable_clips.py --all --dry-run
  
  # Force overwrite existing quotableClips fields
  python add_quotable_clips.py --all --force
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
        help='Overwrite existing quotableClips field if it exists'
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
        
        # Check if quotableClips exists and we're not forcing
        if not args.force:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if content.startswith('---\n'):
                    match = re.search(r'\n---(\n|$)', content[4:])
                    if match:
                        frontmatter_text = content[4:match.start() + 4]
                        frontmatter_data = yaml.safe_load(frontmatter_text)
                        if frontmatter_data and 'quotableClips' in frontmatter_data:
                            # Check if clips are missing endOffset
                            existing_clips = frontmatter_data['quotableClips']
                            has_missing_endoffset = any(
                                isinstance(clip, dict) and 'endOffset' not in clip 
                                for clip in existing_clips
                            )
                            if not has_missing_endoffset:
                                print(f"  ⊘ Skipping (quotableClips already exists with {len(existing_clips)} clips and all have endOffset)")
                                skip_count += 1
                                continue
                            # If endOffset is missing, continue to update
            except Exception:
                # If we can't read it, try to process it anyway
                pass
        
        if add_quotable_clips_to_file(file_path, force=args.force, dry_run=args.dry_run):
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

