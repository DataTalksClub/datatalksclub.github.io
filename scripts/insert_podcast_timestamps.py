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


def update_headers_in_transcript(transcript, timestamps):
    """Update headers in transcript while keeping all content unchanged.
    
    Args:
        transcript: List of transcript entries (with existing headers)
        timestamps: List of (seconds, topic) tuples
        
    Returns:
        Updated transcript with headers replaced/inserted at correct positions
    """
    # Sort timestamps by time
    timestamps = sorted(timestamps, key=lambda x: x[0])
    
    # Build new transcript - keep all content, only update headers
    new_transcript = []
    timestamp_idx = 0
    last_sec = None  # Track the last seen sec value for entries without sec
    next_entry_sec = None  # Track the next entry's sec to better position headers
    
    # First pass: collect all entries with sec to help position headers
    entries_with_sec = []
    for i, entry in enumerate(transcript):
        if 'header' not in entry and entry.get('sec') is not None:
            entries_with_sec.append((i, entry.get('sec')))
    
    def get_next_sec_after_index(idx):
        """Get the next sec value after the given index."""
        for i, entry in enumerate(transcript[idx+1:], start=idx+1):
            if 'header' not in entry and entry.get('sec') is not None:
                return entry.get('sec')
        return None
    
    for i, entry in enumerate(transcript):
        # Skip existing headers - we'll replace them with new ones
        if 'header' in entry:
            continue
        
        # Get entry timestamp - use last_sec if entry doesn't have sec
        entry_sec = entry.get('sec')
        next_sec = get_next_sec_after_index(i)
        
        if entry_sec is not None:
            # Entry has a sec value - use it and update last_sec
            last_sec = entry_sec
            current_sec = entry_sec
        else:
            # Entry doesn't have sec - use last_sec if available
            current_sec = last_sec
        
        # Insert any timestamps that should come before this entry
        # For entries without sec, only insert if timestamp is clearly before next entry
        if current_sec is not None:
            # Insert timestamps that are <= current entry's sec
            while timestamp_idx < len(timestamps):
                timestamp_sec, topic = timestamps[timestamp_idx]
                
                # For entries with sec, insert if timestamp <= entry_sec
                if entry_sec is not None:
                    if timestamp_sec <= entry_sec:
                        new_transcript.append({'header': topic})
                        timestamp_idx += 1
                    else:
                        break
                else:
                    # For entries without sec, insert if timestamp is clearly in the range
                    # between last_sec and next_sec (if next_sec exists)
                    if next_sec is not None:
                        # Insert if timestamp is between last_sec and next_sec
                        if last_sec is not None and last_sec < timestamp_sec <= next_sec:
                            new_transcript.append({'header': topic})
                            timestamp_idx += 1
                        elif timestamp_sec <= last_sec:
                            # Should have been inserted earlier, but insert now
                            new_transcript.append({'header': topic})
                            timestamp_idx += 1
                        else:
                            break
                    else:
                        # No next sec, insert if timestamp > last_sec (new content)
                        if last_sec is not None and timestamp_sec > last_sec:
                            new_transcript.append({'header': topic})
                            timestamp_idx += 1
                        else:
                            break
        
        # Add the transcript entry (content, not headers)
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
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the frontmatter section
        if not content.startswith('---\n'):
            print("Error: File does not start with frontmatter delimiter", file=sys.stderr)
            return False
        
        # Find the closing --- (try both \n---\n and \n---)
        match = re.search(r'\n---\n', content[4:])
        if not match:
            # Try without trailing newline
            match = re.search(r'\n---', content[4:])
        
        if not match:
            print("Error: Could not find closing frontmatter delimiter", file=sys.stderr)
            return False
        
        end_pos = match.start() + 4
        frontmatter_text = content[4:end_pos]
        # Handle both \n---\n and \n--- formats
        if content[end_pos + 4:end_pos + 5] == '\n':
            rest_content = content[end_pos + 5:]
        else:
            rest_content = content[end_pos + 4:]
        
        # Parse frontmatter
        try:
            frontmatter = yaml.safe_load(frontmatter_text)
        except yaml.YAMLError as e:
            print(f"Error: Failed to parse YAML frontmatter: {e}", file=sys.stderr)
            return False
        
        # Check if transcript exists
        if 'transcript' not in frontmatter:
            print("Error: No transcript field found in frontmatter", file=sys.stderr)
            return False
        
        # Update headers while keeping all content unchanged
        updated_transcript = update_headers_in_transcript(frontmatter['transcript'], timestamps)
        
        # Update frontmatter
        frontmatter['transcript'] = updated_transcript
        
        # Convert back to YAML
        try:
            new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
        except Exception as e:
            print(f"Error: Failed to serialize YAML: {e}", file=sys.stderr)
            return False
        
        # Reconstruct file
        new_content = f"---\n{new_frontmatter}---{rest_content}"
        
        # Write back to file
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        except Exception as e:
            print(f"Error: Failed to write file: {e}", file=sys.stderr)
            return False
        
        return True
    
    except Exception as e:
        print(f"Error in update_podcast_file_with_timestamps: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
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
                try:
                    success = update_podcast_file_with_timestamps(file_path, timestamps)
                    if success:
                        print(f"\n✓ File updated successfully with {len(timestamps)} timestamps!")
                    else:
                        print(f"\n✗ Failed to update file", file=sys.stderr)
                        sys.exit(1)
                except Exception as e:
                    print(f"\n✗ Error updating file: {e}", file=sys.stderr)
                    import traceback
                    traceback.print_exc()
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

