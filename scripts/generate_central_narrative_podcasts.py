#!/usr/bin/env python3
"""
Generate titles for podcast episodes using OpenAI API.

This script takes a podcast page, finds the timestamp file from podcast-timestamps folder,
and generates a SEO-optimized title for the podcast episode.

Usage:
    python generate_title_podcasts.py <podcast_file> [--update] [--api-key YOUR_KEY]
    python generate_title_podcasts.py --all-in-dir _podcast/ --update
    python generate_title_podcasts.py --file-list podcasts.txt --update
    
Example:
    python generate_title_podcasts.py _podcast/s01e02-processes.md --update
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List
from openai import OpenAI


DEFAULT_PROMPT = """You are an expert creating a central narrative for a podcast episode.

Task: Determine the single most important idea that unifies all major themes, segments, and discussions in a podcast episode.

REQUIREMENTS:
- Scan all timestamps
- Separate context from core
- Identify the dominant through-line and key themes
- Phrase the center as a clear, high-level theme

TIMESTAMPS:
{timestamps_content}

OUTPUT: Generate ONLY the central narrative text.
"""


def get_timestamps_file(podcast_file_path):
    """Get the timestamp file path for a podcast."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    timestamps_dir = project_root / 'podcast-timestamps'
    
    # Use podcast filename (without .md) for the timestamp file
    podcast_name = podcast_file_path.stem  # filename without extension
    timestamp_file = timestamps_dir / f"{podcast_name}.txt"
    
    return timestamp_file if timestamp_file.exists() else None


def generate_title(timestamps_content, api_key=None):
    """Generate title using OpenAI API."""
    # Initialize OpenAI client
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        # Will use OPENAI_API_KEY environment variable
        client = OpenAI()
    
    # Format the prompt with all the information
    prompt = DEFAULT_PROMPT.format(
        timestamps_content=timestamps_content,
    )

    print(f"Prompt size: {len(prompt)} characters")
    print(f"  - Timestamps: {len(timestamps_content)} characters")
    print()
    
    # Call OpenAI API
    response = client.responses.create(
        model="gpt-5-mini",  # Using gpt-5-mini
        input=prompt,
    )
    
    title = response.output_text.strip()
    
    # Remove quotes if present
    if title.startswith('"') and title.endswith('"'):
        title = title[1:-1]
    if title.startswith("'") and title.endswith("'"):
        title = title[1:-1]
    
    return title


def update_podcast_file(file_path, title):
    """Update the podcast file with the generated title."""
    # Ensure title has no quotes (strip if present)
    title = title.strip()
    if title.startswith('"') and title.endswith('"'):
        title = title[1:-1]
    if title.startswith("'") and title.endswith("'"):
        title = title[1:-1]
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find and replace the title line
    found = False
    for i, line in enumerate(lines):
        if line.strip().startswith('title:'):
            # Always format as: title: "title-here"
            indent = len(line) - len(line.lstrip())
            lines[i] = ' ' * indent + f'title: "{title}"\n'
            found = True
            break
    
    if not found:
        return False
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return True
    

def get_project_root():
    """Get the project root directory (parent of scripts directory)."""
    script_dir = Path(__file__).parent
    return script_dir.parent


def resolve_podcast_path(podcast_file: str) -> Path:
    """Resolve podcast file path relative to project root."""
    file_path = Path(podcast_file)
    if file_path.exists():
        return file_path
    
    # Try relative to project root
    project_root = get_project_root()
    file_path = project_root / podcast_file
    if file_path.exists():
        return file_path
    
    return None


def get_podcast_files_from_args(args) -> List[Path]:
    """Get list of podcast files from command line arguments."""
    files = []
    
    if args.file_list:
        # Read from file
        list_file = Path(args.file_list)
        if not list_file.exists():
            project_root = get_project_root()
            list_file = project_root / args.file_list
        
        if not list_file.exists():
            print(f"Error: File list not found: {args.file_list}", file=sys.stderr)
            sys.exit(1)
        
        with open(list_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    file_path = resolve_podcast_path(line)
                    if file_path:
                        files.append(file_path)
                    else:
                        print(f"Warning: File not found: {line}", file=sys.stderr)
    
    elif args.all_in_dir:
        # Get all .md files in directory
        project_root = get_project_root()
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
    
    return files


def process_podcast_file(podcast_file: Path, api_key: str = None, update: bool = False, dry_run: bool = False) -> bool:
    """Process a single podcast file to generate and optionally update the title."""
    print(f"Processing: {podcast_file.name}")
    print("-" * 60)
    
    try:
        # Get timestamp file
        timestamp_file = get_timestamps_file(podcast_file)
        if not timestamp_file:
            print(f"Warning: Timestamp file not found: podcast-timestamps/{podcast_file.stem}.txt", file=sys.stderr)
            timestamps_content = "No timestamps available."
        else:
            print(f"Found timestamps: {timestamp_file.relative_to(timestamp_file.parent.parent)}")
            with open(timestamp_file, 'r', encoding='utf-8') as f:
                timestamps_content = f.read().strip()
        
        print()
        print("Generating title...")
        print()
        
        # Generate title
        title = generate_title(timestamps_content, api_key=api_key)
        
        print(f"Generated title ({len(title)} chars):")
        print(f"  {title}")
        print()
        
        # Update file if requested
        if update:
            if dry_run:
                print("\n[DRY RUN] Would update the file with the new title")
                return True
            else:
                success = update_podcast_file(podcast_file, title)
                if success:
                    print(f"\n✓ File updated successfully!")
                    return True
                else:
                    print(f"\n✗ Failed to update file", file=sys.stderr)
                    return False
        else:
            print("\nTo update the file, run with --update flag")
            return True
    
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Generate titles for podcast episodes using OpenAI API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate title and display it
  python generate_title_podcasts.py _podcast/s01e02-processes.md
  
  # Generate and update the file
  python generate_title_podcasts.py _podcast/s01e02-processes.md --update
  
  # Process multiple files
  python generate_title_podcasts.py _podcast/episode1.md _podcast/episode2.md --update
  
  # Process all files in a directory
  python generate_title_podcasts.py --all-in-dir _podcast/ --update
  
  # Read file list from a text file
  python generate_title_podcasts.py --file-list podcasts.txt --update
  
  # Use custom API key
  python generate_title_podcasts.py _podcast/s01e02-processes.md --api-key sk-...
  
  # Dry run to see what would be done
  python generate_title_podcasts.py --all-in-dir _podcast/ --dry-run
        """
    )
    
    parser.add_argument('podcast_files', nargs='*', help='Podcast markdown files to process')
    parser.add_argument('--file-list', help='Text file containing list of podcast files (one per line)')
    parser.add_argument('--all-in-dir', help='Process all .md files in the specified directory')
    parser.add_argument('--update', action='store_true', help='Update the file with generated title')
    parser.add_argument('--api-key', help='OpenAI API key (or set OPENAI_API_KEY env var)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.podcast_files and not args.file_list and not args.all_in_dir:
        parser.error("Must provide podcast files, --file-list, or --all-in-dir")
    
    # Get list of files to process
    files = get_podcast_files_from_args(args)
    
    if not files:
        print("Error: No valid podcast files found", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(files)} podcast file(s) to process")
    if args.dry_run:
        print("[DRY RUN MODE - No changes will be made]")
    print()
    
    # Use API key from environment if not provided
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    
    # Process each file
    successful = 0
    failed = 0
    
    for i, podcast_file in enumerate(files, 1):
        print(f"\n[{i}/{len(files)}] ", end='')
        success = process_podcast_file(
            podcast_file,
            api_key=api_key,
            update=args.update,
            dry_run=args.dry_run
        )
        
        if success:
            successful += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Summary: {successful} successful, {failed} failed")
    
    if failed > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()

