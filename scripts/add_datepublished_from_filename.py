#!/usr/bin/env python3
"""
Add datepublished field to blog post files based on filename.

This script extracts the date from the blog post filename (YYYY-MM-DD format)
and adds a 'datepublished' field to the frontmatter. If the 'date' field doesn't
exist, it will also be set equal to datepublished.

Usage:
    python add_datepublished_from_filename.py
    python add_datepublished_from_filename.py --dry-run
    python add_datepublished_from_filename.py --force
"""

import argparse
import re
import sys
import yaml
from pathlib import Path
from typing import Optional


def get_project_root() -> Path:
    """Return the project root directory (parent of scripts directory)."""
    return Path(__file__).parent.parent


def extract_date_from_filename(filename: str) -> Optional[str]:
    """
    Extract date from filename in YYYY-MM-DD format.
    Expected format: YYYY-MM-DD-title.md
    """
    # Match YYYY-MM-DD at the start of filename
    match = re.match(r'^(\d{4}-\d{2}-\d{2})', filename)
    if match:
        date_str = match.group(1)
        # Validate the date format
        try:
            # Try to parse to ensure it's a valid date
            from datetime import datetime
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            return None
    return None


def add_datepublished_to_file(file_path: Path, force: bool = False, dry_run: bool = False) -> bool:
    """
    Add datepublished field to a blog post file's frontmatter.
    If date field doesn't exist, also add it equal to datepublished.
    
    Args:
        file_path: Path to the blog post markdown file
        force: If True, overwrite existing datepublished field
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
    
    # Extract date from filename
    date_published = extract_date_from_filename(file_path.name)
    if not date_published:
        print(f"  ✗ Could not extract date from filename: {file_path.name}")
        return False
    
    # Track what we're doing
    added_datepublished = False
    added_date = False
    changes_made = False
    
    # Add or update datepublished field if needed
    if 'datepublished' not in frontmatter_data or force:
        frontmatter_data['datepublished'] = date_published
        added_datepublished = True
        changes_made = True
    
    # If date field doesn't exist, set it equal to datepublished
    if 'date' not in frontmatter_data:
        # Use datepublished if it exists, otherwise use the extracted date
        date_value = frontmatter_data.get('datepublished', date_published)
        frontmatter_data['date'] = date_value
        added_date = True
        changes_made = True
    
    # If no changes needed, skip
    if not changes_made:
        if 'datepublished' in frontmatter_data and 'date' in frontmatter_data:
            print(f"  ⊘ Skipping (datepublished and date already exist)")
        return True
    
    # Print what we're doing
    if dry_run:
        if added_datepublished:
            print(f"  [DRY RUN] Would add datepublished: {date_published}")
        if added_date:
            print(f"  [DRY RUN] Would add date: {frontmatter_data['date']} (equal to datepublished)")
        if not added_date and 'date' in frontmatter_data:
            print(f"  [DRY RUN] Would skip date (already exists: {frontmatter_data['date']})")
    else:
        if added_datepublished:
            print(f"  ✓ Added datepublished: {date_published}")
        if added_date:
            print(f"  ✓ Added date: {frontmatter_data['date']} (equal to datepublished)")
        if not added_date and 'date' in frontmatter_data:
            print(f"  ⊘ Skipped date (already exists: {frontmatter_data['date']})")

    if dry_run:
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
        return True
    except Exception as e:
        print(f"  ✗ Error writing file: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Add datepublished field to blog post files based on filename',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process all blog posts
  python add_datepublished_from_filename.py
  
  # Dry run to see what would be done
  python add_datepublished_from_filename.py --dry-run
  
  # Force overwrite existing datepublished fields
  python add_datepublished_from_filename.py --force
        """
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without updating files'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='Overwrite existing datepublished field if it exists'
    )
    
    args = parser.parse_args()
    
    # Get project root and posts directory
    project_root = get_project_root()
    posts_dir = project_root / '_posts'
    
    if not posts_dir.exists():
        print(f"Error: Posts directory not found: {posts_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Get all markdown files in _posts directory
    files = sorted(posts_dir.glob('*.md'))
    
    if not files:
        print("No blog post files found.", file=sys.stderr)
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
        
        if add_datepublished_to_file(file_path, force=args.force, dry_run=args.dry_run):
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

