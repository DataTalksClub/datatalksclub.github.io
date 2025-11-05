#!/usr/bin/env python3
"""
Batch generate and insert timestamps for multiple podcast episodes.

This script:
1. Generates timestamps using AI for each podcast file
2. Automatically inserts them into the transcript

Usage:
    python batch_generate_and_insert_timestamps.py <podcast_file1> <podcast_file2> ...
    python batch_generate_and_insert_timestamps.py --file-list list.txt
    python batch_generate_and_insert_timestamps.py --all-in-dir _podcast/to-update-top-10/
    
Options:
    --file-list FILE    Read list of podcast files from a text file (one per line)
    --all-in-dir DIR    Process all .md files in the specified directory
    --skip-insert       Only generate timestamps, don't insert them
    --api-key KEY       OpenAI API key (or set OPENAI_API_KEY env var)
    --dry-run           Show what would be done without making changes
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
from typing import List


def get_project_root():
    """Get the project root directory (parent of scripts directory)."""
    script_dir = Path(__file__).parent
    return script_dir.parent


def resolve_podcast_path(podcast_file: str) -> Path:
    """Resolve podcast file path relative to project root."""
    project_root = get_project_root()
    file_path = Path(podcast_file)
    
    if file_path.exists():
        return file_path.resolve()
    
    # Try relative to project root
    file_path = project_root / podcast_file
    if file_path.exists():
        return file_path.resolve()
    
    return None


def generate_timestamps(podcast_file: Path, api_key: str = None, dry_run: bool = False) -> Path:
    """Generate timestamps for a podcast file."""
    project_root = get_project_root()
    script_path = project_root / 'scripts' / 'generate_podcast_timestamps.py'
    
    # Build command
    cmd = [sys.executable, str(script_path), str(podcast_file)]
    if api_key:
        cmd.extend(['--api-key', api_key])
    
    if dry_run:
        print(f"  [DRY RUN] Would generate timestamps for: {podcast_file.name}")
        return None
    
    print(f"  Generating timestamps...", end=' ', flush=True)
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        
        # Find the generated timestamp file
        podcast_name = podcast_file.stem
        timestamps_file = project_root / 'podcast-timestamps' / f"{podcast_name}.txt"
        
        if timestamps_file.exists():
            print("✓")
            return timestamps_file
        else:
            print("✗ (file not created)")
            return None
            
    except subprocess.CalledProcessError as e:
        print(f"✗ (error)")
        print(f"    Error: {e.stderr}", file=sys.stderr)
        return None


def insert_timestamps(podcast_file: Path, timestamps_file: Path, dry_run: bool = False) -> bool:
    """Insert timestamps into podcast transcript."""
    project_root = get_project_root()
    script_path = project_root / 'scripts' / 'insert_podcast_timestamps.py'
    
    # Build command
    cmd = [
        sys.executable,
        str(script_path),
        str(podcast_file),
        '--timestamps-file',
        str(timestamps_file),
        '--update'
    ]
    
    if dry_run:
        print(f"  [DRY RUN] Would insert timestamps into: {podcast_file.name}")
        return True
    
    print(f"  Inserting timestamps...", end=' ', flush=True)
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        print("✓")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"✗ (error)")
        print(f"    Error: {e.stderr}", file=sys.stderr)
        return False


def process_podcast_file(podcast_file: Path, api_key: str = None, skip_insert: bool = False, dry_run: bool = False) -> bool:
    """Process a single podcast file: generate and insert timestamps."""
    print(f"\nProcessing: {podcast_file.name}")
    print("-" * 60)
    
    # Step 1: Generate timestamps
    timestamps_file = generate_timestamps(podcast_file, api_key, dry_run)
    
    if not timestamps_file:
        print(f"  ✗ Failed to generate timestamps")
        return False
    
    if skip_insert:
        print(f"  → Timestamps saved to: {timestamps_file.relative_to(get_project_root())}")
        return True
    
    # Step 2: Insert timestamps
    success = insert_timestamps(podcast_file, timestamps_file, dry_run)
    
    if success:
        print(f"  ✓ Successfully processed: {podcast_file.name}")
    else:
        print(f"  ✗ Failed to insert timestamps")
    
    return success


def get_podcast_files_from_args(args) -> List[Path]:
    """Get list of podcast files from command line arguments."""
    files = []
    
    if args.file_list:
        # Read from file
        list_file = Path(args.file_list)
        if not list_file.exists():
            # Try relative to project root
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
                sys.exit(1)
    
    return files


def main():
    parser = argparse.ArgumentParser(
        description='Batch generate and insert timestamps for podcast episodes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process specific files
  python batch_generate_and_insert_timestamps.py _podcast/episode1.md _podcast/episode2.md
  
  # Process all files in a directory
  python batch_generate_and_insert_timestamps.py --all-in-dir _podcast/to-update-top-10/
  
  # Read file list from a text file
  python batch_generate_and_insert_timestamps.py --file-list podcasts.txt
  
  # Only generate timestamps, don't insert
  python batch_generate_and_insert_timestamps.py --all-in-dir _podcast/to-update-top-10/ --skip-insert
  
  # Dry run to see what would be done
  python batch_generate_and_insert_timestamps.py --all-in-dir _podcast/to-update-top-10/ --dry-run
        """
    )
    
    parser.add_argument('podcast_files', nargs='*', help='Podcast markdown files to process')
    parser.add_argument('--file-list', help='Text file containing list of podcast files (one per line)')
    parser.add_argument('--all-in-dir', help='Process all .md files in the specified directory')
    parser.add_argument('--skip-insert', action='store_true', help='Only generate timestamps, don\'t insert them')
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
            skip_insert=args.skip_insert,
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

