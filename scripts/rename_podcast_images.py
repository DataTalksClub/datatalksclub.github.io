#!/usr/bin/env python3
"""
Script to rename podcast images according to updated podcast filenames.

This script:
1. Reads the podcast rename mapping from scripts/podcast-rename-mapping.md
2. Renames image files in images/podcast/ directory
3. Updates image references in podcast markdown files
"""

import re
import sys
from pathlib import Path
from typing import Dict, Tuple


def parse_mapping_file(mapping_file: Path) -> Dict[str, str]:
    """
    Parse the markdown mapping file and extract old -> new name mappings.
    
    Returns a dictionary mapping old names (without .md) to new names (without .md).
    Note: Some new names may contain .md in the middle (e.g., "name.md.md" becomes "name.md").
    """
    mappings = {}
    
    if not mapping_file.exists():
        print(f"Error: Mapping file not found: {mapping_file}", file=sys.stderr)
        sys.exit(1)
    
    with open(mapping_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Match markdown table rows: | `old-name.md` | `new-name.md` |
            # The regex captures everything before the final .md
            match = re.match(r'^\|\s*`([^`]+)\.md`\s*\|\s*`([^`]+)\.md`\s*\|', line)
            if match:
                old_name = match.group(1)
                new_name = match.group(2)  # This may contain .md in the middle
                mappings[old_name] = new_name
    
    return mappings


def rename_image_file(old_path: Path, new_path: Path, dry_run: bool = False) -> bool:
    """Rename an image file."""
    if not old_path.exists():
        print(f"Warning: Image file not found: {old_path}")
        return False
    
    if new_path.exists():
        print(f"Warning: Target image file already exists: {new_path}")
        return False
    
    if dry_run:
        print(f"Would rename: {old_path} -> {new_path}")
        return True
    
    try:
        old_path.rename(new_path)
        print(f"Renamed: {old_path.name} -> {new_path.name}")
        return True
    except Exception as e:
        print(f"Error renaming {old_path}: {e}", file=sys.stderr)
        return False


def update_podcast_file_references(
    podcast_file: Path,
    old_image_name: str,
    new_image_name: str,
    dry_run: bool = False
) -> bool:
    """Update image references in a podcast markdown file."""
    if not podcast_file.exists():
        return False
    
    try:
        with open(podcast_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match image references like:
        # image: images/podcast/old-name.jpg
        old_pattern = f'images/podcast/{old_image_name}.jpg'
        new_pattern = f'images/podcast/{new_image_name}.jpg'
        
        if old_pattern in content:
            new_content = content.replace(old_pattern, new_pattern)
            
            if dry_run:
                print(f"Would update image reference in: {podcast_file.name}")
                print(f"  {old_pattern} -> {new_pattern}")
            else:
                with open(podcast_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated image reference in: {podcast_file.name}")
            return True
        
        return False
    except Exception as e:
        print(f"Error updating {podcast_file}: {e}", file=sys.stderr)
        return False


def main():
    """Main function to rename podcast images."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Rename podcast images according to updated podcast filenames'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    parser.add_argument(
        '--mapping-file',
        type=Path,
        default=Path(__file__).parent / 'podcast-rename-mapping.md',
        help='Path to the mapping file (default: scripts/podcast-rename-mapping.md)'
    )
    parser.add_argument(
        '--images-dir',
        type=Path,
        default=Path(__file__).parent.parent / 'images' / 'podcast',
        help='Path to podcast images directory (default: images/podcast)'
    )
    parser.add_argument(
        '--podcast-dir',
        type=Path,
        default=Path(__file__).parent.parent / '_podcast',
        help='Path to podcast markdown files directory (default: _podcast)'
    )
    
    args = parser.parse_args()
    
    # Get project root
    project_root = Path(__file__).parent.parent
    
    # Parse mappings
    print(f"Reading mappings from: {args.mapping_file}")
    mappings = parse_mapping_file(args.mapping_file)
    print(f"Found {len(mappings)} mappings\n")
    
    if not mappings:
        print("No mappings found. Exiting.")
        sys.exit(1)
    
    # Track statistics
    images_renamed = 0
    images_not_found = 0
    references_updated = 0
    
    # Process each mapping
    for old_name, new_name in sorted(mappings.items()):
        print(f"\nProcessing: {old_name} -> {new_name}")
        
        # Rename image file
        old_image_path = args.images_dir / f"{old_name}.jpg"
        new_image_path = args.images_dir / f"{new_name}.jpg"
        
        if rename_image_file(old_image_path, new_image_path, args.dry_run):
            images_renamed += 1
        else:
            images_not_found += 1
        
        # Update references in podcast markdown file
        podcast_file = args.podcast_dir / f"{new_name}.md"
        if update_podcast_file_references(podcast_file, old_name, new_name, args.dry_run):
            references_updated += 1
    
    # Print summary
    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Images renamed: {images_renamed}")
    print(f"  Images not found: {images_not_found}")
    print(f"  References updated: {references_updated}")
    if args.dry_run:
        print("\n  (Dry run - no files were actually changed)")
    print("=" * 60)


if __name__ == '__main__':
    main()

