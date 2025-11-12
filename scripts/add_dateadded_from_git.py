#!/usr/bin/env python3
"""
Add dateadded field to podcast files based on git file creation history.

This script uses git log to determine when each podcast file was first added to the repository
and adds a 'dateadded' field to the frontmatter.

Usage:
    python add_dateadded_from_git.py <podcast_file1> <podcast_file2> ...
    python add_dateadded_from_git.py --all-in-dir _podcast/
    python add_dateadded_from_git.py --all

Options:
    --all-in-dir DIR  Process all .md files in the specified directory
    --all             Process all podcast files in _podcast/
    --dry-run         Show what would be done without updating files
    --force           Overwrite existing dateadded field if it exists
"""

import argparse
import re
import subprocess
import sys
import yaml
from datetime import datetime
from pathlib import Path
from typing import List, Optional


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


def get_file_creation_date(file_path: Path) -> Optional[str]:
    """
    Get the date when a file was first added to git.
    Returns the date in YYYY-MM-DD format, or None if not found.
    """
    project_root = get_project_root()
    # Get relative path from project root
    try:
        rel_path = file_path.relative_to(project_root)
    except ValueError:
        # File is not under project root
        return None

    # Use git log to find when file was first added (--diff-filter=A means "Added")
    cmd = [
        'git',
        'log',
        '--format=%ai',
        '--diff-filter=A',
        '--',
        str(rel_path)
    ]

    try:
        result = subprocess.run(
            cmd,
            cwd=project_root,
            capture_output=True,
            text=True,
            check=True
        )
        
        if result.stdout.strip():
            # Get the last line (oldest commit, which is when file was added)
            date_str = result.stdout.strip().split('\n')[-1]
            # Parse the date and return in YYYY-MM-DD format
            # Format is: "2021-02-23 12:01:20 +0100"
            date_obj = datetime.strptime(date_str.split('+')[0].strip(), '%Y-%m-%d %H:%M:%S')
            return date_obj.strftime('%Y-%m-%d')
    except subprocess.CalledProcessError:
        # File might not be in git history
        return None
    except ValueError:
        # Date parsing failed
        return None

    return None


def add_dateadded_to_file(file_path: Path, force: bool = False, dry_run: bool = False) -> bool:
    """
    Add dateadded field to a podcast file's frontmatter.
    
    Args:
        file_path: Path to the podcast markdown file
        force: If True, overwrite existing dateadded field
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
    
    # Check if dateadded already exists
    if 'dateadded' in frontmatter_data and not force:
        print(f"  ⊘ Skipping (dateadded already exists: {frontmatter_data['dateadded']})")
        return True

    # Get creation date from git
    creation_date = get_file_creation_date(file_path)
    if not creation_date:
        print(f"  ✗ Could not determine file creation date from git")
        return False

    # Add or update dateadded field
    frontmatter_data['dateadded'] = creation_date

    if dry_run:
        print(f"  [DRY RUN] Would add dateadded: {creation_date}")
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
        print(f"  ✓ Added dateadded: {creation_date}")
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
        description='Add dateadded field to podcast files based on git history',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process specific files
  python add_dateadded_from_git.py _podcast/s01e01-roles.md _podcast/s01e02-processes.md
  
  # Process all files in a directory
  python add_dateadded_from_git.py --all-in-dir _podcast/
  
  # Process all podcast files
  python add_dateadded_from_git.py --all
  
  # Dry run to see what would be done
  python add_dateadded_from_git.py --all --dry-run
  
  # Force overwrite existing dateadded fields
  python add_dateadded_from_git.py --all --force
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
        help='Overwrite existing dateadded field if it exists'
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
        
        # Check if dateadded exists and we're not forcing
        if not args.force:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if content.startswith('---\n'):
                    match = re.search(r'\n---(\n|$)', content[4:])
                    if match:
                        frontmatter_text = content[4:match.start() + 4]
                        frontmatter_data = yaml.safe_load(frontmatter_text)
                        if frontmatter_data and 'dateadded' in frontmatter_data:
                            print(f"  ⊘ Skipping (dateadded already exists: {frontmatter_data['dateadded']})")
                            skip_count += 1
                            continue
            except Exception:
                # If we can't read it, try to process it anyway
                pass
        
        if add_dateadded_to_file(file_path, force=args.force, dry_run=args.dry_run):
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

