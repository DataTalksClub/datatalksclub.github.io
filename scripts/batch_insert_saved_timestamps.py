#!/usr/bin/env python3
"""
Batch insert previously generated timestamps into podcast transcripts.

This script looks for timestamp files in the `podcast-timestamps/` directory
(or a custom directory) that match the name of each podcast markdown file and
inserts them into the transcript using `insert_podcast_timestamps.py`.

Usage:
    python batch_insert_saved_timestamps.py <podcast_file1> <podcast_file2> ...
    python batch_insert_saved_timestamps.py --file-list list.txt
    python batch_insert_saved_timestamps.py --all-in-dir _podcast/no-timestamps/

Options:
    --timestamps-dir DIR  Directory containing timestamp .txt files (default: podcast-timestamps)
    --dry-run             Show what would be done without updating files
"""

import argparse
import os
import sys
import subprocess
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


def find_timestamps_file(podcast_file: Path, timestamps_dir: Path) -> Optional[Path]:
    """Return the timestamps file that matches the podcast file stem."""
    podcast_name = podcast_file.stem
    candidate = timestamps_dir / f"{podcast_name}.txt"
    if candidate.exists():
        return candidate.resolve()
    return None


def insert_timestamps(podcast_file: Path, timestamps_file: Path, dry_run: bool = False) -> bool:
    """Run the insert_podcast_timestamps.py script for the given files."""
    script_path = get_project_root() / 'scripts' / 'insert_podcast_timestamps.py'

    cmd = [
        sys.executable,
        str(script_path),
        str(podcast_file),
        '--timestamps-file',
        str(timestamps_file),
        '--update',
    ]

    if dry_run:
        print(f"  [DRY RUN] Would insert timestamps from {timestamps_file.name} into {podcast_file.name}")
        return True

    print("  Inserting timestamps...", end=' ', flush=True)
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("✓")
        return True
    except subprocess.CalledProcessError as exc:
        print("✗ (error)")
        if exc.stdout:
            print(f"    stdout: {exc.stdout.strip()}", file=sys.stderr)
        if exc.stderr:
            print(f"    stderr: {exc.stderr.strip()}", file=sys.stderr)
        return False


def get_podcast_files_from_args(args: argparse.Namespace) -> List[Path]:
    """Collect podcast files based on CLI arguments."""
    files: List[Path] = []

    if args.file_list:
        list_path = Path(args.file_list)
        if not list_path.exists():
            list_path = get_project_root() / args.file_list

        if not list_path.exists():
            print(f"Error: File list not found: {args.file_list}", file=sys.stderr)
            sys.exit(1)

        with open(list_path, 'r', encoding='utf-8') as handle:
            for line in handle:
                entry = line.strip()
                if not entry or entry.startswith('#'):
                    continue
                resolved = resolve_podcast_path(entry)
                if resolved:
                    files.append(resolved)
                else:
                    print(f"Warning: File not found: {entry}", file=sys.stderr)

    elif args.all_in_dir:
        base_dir = Path(args.all_in_dir)
        if not base_dir.is_absolute():
            base_dir = get_project_root() / args.all_in_dir

        if not base_dir.exists():
            print(f"Error: Directory not found: {args.all_in_dir}", file=sys.stderr)
            sys.exit(1)

        files = sorted(base_dir.glob('*.md'))

    else:
        for podcast_file in args.podcast_files:
            resolved = resolve_podcast_path(podcast_file)
            if resolved:
                files.append(resolved)
            else:
                print(f"Error: File not found: {podcast_file}", file=sys.stderr)
                sys.exit(1)

    return files


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Batch insert timestamps from saved files into podcast transcripts',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process specific files
  python batch_insert_saved_timestamps.py _podcast/no-timestamps/episode1.md _podcast/no-timestamps/episode2.md

  # Process all files in a directory
  python batch_insert_saved_timestamps.py --all-in-dir _podcast/no-timestamps/

  # Read file list from a text file
  python batch_insert_saved_timestamps.py --file-list podcasts.txt

  # Dry run to preview actions
  python batch_insert_saved_timestamps.py --all-in-dir _podcast/no-timestamps/ --dry-run
        """,
    )

    parser.add_argument('podcast_files', nargs='*', help='Podcast markdown files to process')
    parser.add_argument('--file-list', help='Text file containing list of podcast files (one per line)')
    parser.add_argument('--all-in-dir', help='Process all .md files in the specified directory')
    parser.add_argument('--timestamps-dir', default='podcast-timestamps', help='Directory with timestamp .txt files')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without updating files')

    args = parser.parse_args()

    if not args.podcast_files and not args.file_list and not args.all_in_dir:
        parser.error("Must provide podcast files, --file-list, or --all-in-dir")

    files = get_podcast_files_from_args(args)
    if not files:
        print("Error: No valid podcast files found", file=sys.stderr)
        sys.exit(1)

    project_root = get_project_root()
    timestamps_dir = Path(args.timestamps_dir)
    if not timestamps_dir.is_absolute():
        timestamps_dir = project_root / args.timestamps_dir

    if not timestamps_dir.exists():
        print(f"Error: Timestamps directory not found: {timestamps_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(files)} podcast file(s) to process")
    if args.dry_run:
        print("[DRY RUN MODE - No changes will be made]")

    successes = 0
    failures = 0
    skipped = 0

    for idx, podcast_file in enumerate(files, start=1):
        print(f"\n[{idx}/{len(files)}] Processing: {podcast_file.name}")
        print("-" * 60)

        timestamps_file = find_timestamps_file(podcast_file, timestamps_dir)
        if not timestamps_file:
            print(f"  ✗ No timestamps file found for {podcast_file.stem} in {timestamps_dir}")
            skipped += 1
            continue

        print(f"  Using timestamps file: {timestamps_file.name}")
        if insert_timestamps(podcast_file, timestamps_file, dry_run=args.dry_run):
            successes += 1
        else:
            failures += 1

    print("\n" + "=" * 60)
    print(f"Summary: {successes} successful, {failures} failed, {skipped} skipped")

    if failures > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()

