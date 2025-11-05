#!/usr/bin/env python3
"""
Insert timestamps into podcast transcript from a text file.

This script removes existing timestamp headers from the transcript and inserts
new ones at the correct positions based on timing.

Usage:
    python insert_podcast_timestamps.py <podcast_file> --timestamps-file <timestamps.txt> [--update]
    
Example:
    python insert_podcast_timestamps.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md --timestamps-file timestamps.txt --update
"""

import os
import sys
import yaml
import argparse
import re
from pathlib import Path


def parse_timestamps_file(timestamps_file_path):
    """Parse a timestamps file and return list of (seconds, topic) tuples.
    
    Expected format: HH:MM:SS Topic text
    Example: 00:01:12 Podcasts Overview: Vanishing Gradients and High Signal
    """
    timestamps = []
    
    with open(timestamps_file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
                
            # Match pattern: HH:MM:SS Topic
            match = re.match(r'^(\d{2}):(\d{2}):(\d{2})\s+(.+)$', line)
            if not match:
                print(f"Warning: Skipping line {line_num} (invalid format): {line}", file=sys.stderr)
                continue
            
            hours, minutes, seconds, topic = match.groups()
            total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
            timestamps.append((total_seconds, topic.strip()))
    
    return timestamps


def remove_existing_headers(transcript):
    """Remove all header entries from transcript list."""
    return [entry for entry in transcript if 'header' not in entry]


def insert_timestamps_into_transcript(transcript, timestamps):
    """Insert timestamp headers into transcript at appropriate positions.
    
    Args:
        transcript: List of transcript entries (without headers)
        timestamps: List of (seconds, topic) tuples
        
    Returns:
        Updated transcript with headers inserted
    """
    # Sort timestamps by time
    timestamps = sorted(timestamps, key=lambda x: x[0])
    
    # Build new transcript with headers
    new_transcript = []
    timestamp_idx = 0
    
    for entry in transcript:
        # Insert any timestamps that should come before this entry
        entry_sec = entry.get('sec', float('inf'))
        
        while timestamp_idx < len(timestamps) and timestamps[timestamp_idx][0] <= entry_sec:
            sec, topic = timestamps[timestamp_idx]
            new_transcript.append({'header': topic})
            timestamp_idx += 1
        
        # Add the transcript entry
        new_transcript.append(entry)
    
    # Add any remaining timestamps at the end
    while timestamp_idx < len(timestamps):
        sec, topic = timestamps[timestamp_idx]
        new_transcript.append({'header': topic})
        timestamp_idx += 1
    
    return new_transcript


def update_podcast_file_with_timestamps(file_path, timestamps):
    """Update the podcast file with new timestamps in the transcript.
    
    Args:
        file_path: Path to the podcast markdown file
        timestamps: List of (seconds, topic) tuples
        
    Returns:
        True if successful, False otherwise
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the frontmatter section
    if content.startswith('---\n'):
        # Find the closing ---
        match = re.search(r'\n---\n', content[4:])
        if match:
            end_pos = match.start() + 4
            frontmatter_text = content[4:end_pos]
            rest_content = content[end_pos + 5:]
            
            # Parse frontmatter
            frontmatter = yaml.safe_load(frontmatter_text)
            
            # Check if transcript exists
            if 'transcript' not in frontmatter:
                print("Error: No transcript field found in frontmatter", file=sys.stderr)
                return False
            
            # Remove existing headers
            transcript_without_headers = remove_existing_headers(frontmatter['transcript'])
            
            # Insert new timestamps
            updated_transcript = insert_timestamps_into_transcript(transcript_without_headers, timestamps)
            
            # Update frontmatter
            frontmatter['transcript'] = updated_transcript
            
            # Convert back to YAML
            new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
            
            # Reconstruct file
            new_content = f"---\n{new_frontmatter}---{rest_content}"
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
    
    return False


def main():
    parser = argparse.ArgumentParser(
        description='Insert timestamps into podcast transcript',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview timestamps without updating
  python insert_podcast_timestamps.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md --timestamps-file timestamps.txt
  
  # Insert timestamps and update the file
  python insert_podcast_timestamps.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md --timestamps-file timestamps.txt --update
  
  # Dry run to see what would be done
  python insert_podcast_timestamps.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md --timestamps-file timestamps.txt --dry-run
        """
    )
    
    parser.add_argument('podcast_file', help='Path to the podcast markdown file')
    parser.add_argument('--timestamps-file', required=True, help='Path to text file containing timestamps (HH:MM:SS Topic format)')
    parser.add_argument('--update', action='store_true', help='Update the file with timestamps')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    # Resolve file paths - try relative to current dir, then relative to project root
    file_path = Path(args.podcast_file)
    if not file_path.exists():
        # If not found, try relative to project root (where script is located)
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        file_path = project_root / args.podcast_file
    
    if not file_path.exists():
        print(f"Error: File not found: {args.podcast_file}", file=sys.stderr)
        sys.exit(1)
    
    timestamps_file = Path(args.timestamps_file)
    if not timestamps_file.exists():
        # Try relative to current directory first, then project root
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        timestamps_file = project_root / args.timestamps_file
    
    if not timestamps_file.exists():
        print(f"Error: Timestamps file not found: {args.timestamps_file}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing: {file_path.name}")
    print("-" * 60)
    
    try:
        print(f"Reading timestamps from: {timestamps_file.name}")
        timestamps = parse_timestamps_file(timestamps_file)
        
        if not timestamps:
            print("Error: No valid timestamps found in file", file=sys.stderr)
            sys.exit(1)
        
        print(f"\nParsed {len(timestamps)} timestamps:")
        for sec, topic in timestamps[:5]:  # Show first 5
            hours = sec // 3600
            minutes = (sec % 3600) // 60
            seconds = sec % 60
            print(f"  {hours:02d}:{minutes:02d}:{seconds:02d} {topic}")
        if len(timestamps) > 5:
            print(f"  ... and {len(timestamps) - 5} more")
        print()
        
        # Update file if requested
        if args.update:
            if args.dry_run:
                print("[DRY RUN] Would update the file with new timestamps")
            else:
                print("Updating podcast file with timestamps...")
                success = update_podcast_file_with_timestamps(file_path, timestamps)
                if success:
                    print(f"\n✓ File updated successfully with {len(timestamps)} timestamps!")
                else:
                    print(f"\n✗ Failed to update file", file=sys.stderr)
                    sys.exit(1)
        else:
            print("To update the file, run with --update flag")
    
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

