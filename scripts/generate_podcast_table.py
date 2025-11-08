#!/usr/bin/env python3
"""
Generate a CSV table with podcast title, DTC website link, YouTube link, and timestamps
for all podcasts that have timestamp files.
"""

import sys
import yaml
import re
import csv
from pathlib import Path


def parse_podcast_file(file_path):
    """Parse a podcast markdown file and extract front matter."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract front matter - look for ---\n at start and ---\n or --- at end
    if content.startswith('---\n'):
        # Try to find the closing ---
        # Look for \n---\n (most common) or \n--- at end of content
        match = re.search(r'\n---(\n|$)', content[4:])
        if match:
            end_pos = match.start() + 4
            frontmatter_text = content[4:end_pos]
            
            try:
                frontmatter = yaml.safe_load(frontmatter_text)
                return frontmatter
            except yaml.YAMLError as e:
                return None
    
    return None




def main():
    # Get project root (parent of scripts directory)
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Get all timestamp files
    timestamps_dir = project_root / "podcast-timestamps"
    timestamp_files = sorted(timestamps_dir.glob("*.txt"))
    
    # Collect podcast information
    podcasts = []
    for timestamp_file in timestamp_files:
        # Use absolute path for podcast file lookup
        podcast_filename = timestamp_file.stem
        podcast_file = project_root / "_podcast" / f"{podcast_filename}.md"
        
        if not podcast_file.exists():
            print(f"Warning: Could not find podcast file for {timestamp_file.name}", file=sys.stderr)
            continue
        
        # Parse the podcast markdown file
        frontmatter = parse_podcast_file(podcast_file)
        if not frontmatter:
            print(f"Warning: Could not parse frontmatter for {timestamp_file.name}", file=sys.stderr)
            continue
        
        # Extract information
        title = frontmatter.get('title', 'N/A')
        youtube_link = frontmatter.get('links', {}).get('youtube', 'N/A')
        intro = frontmatter.get('intro', 'N/A')
        
        # Handle multi-line intro (convert to single line, preserving content)
        if isinstance(intro, str):
            # Replace <br><br> with spaces, normalize whitespace
            intro = intro.replace('<br><br>', ' ').replace('<br>', ' ')
            intro = ' '.join(intro.split())  # Normalize whitespace
        elif intro == 'N/A':
            pass  # Keep as is
        else:
            intro = str(intro) if intro else 'N/A'
        
        # Generate DTC website link
        dtc_link = f"https://datatalks.club/podcast/{podcast_filename}.html"
        
        # Read timestamps content
        try:
            with open(timestamp_file, 'r', encoding='utf-8') as f:
                timestamps_content = f.read().strip()
        except Exception as e:
            print(f"Warning: Could not read timestamps file {timestamp_file.name}: {e}", file=sys.stderr)
            timestamps_content = 'N/A'
        
        podcasts.append({
            'title': title,
            'dtc_link': dtc_link,
            'youtube_link': youtube_link,
            'intro': intro,
            'timestamps': timestamps_content
        })
    
    # Generate CSV output
    writer = csv.writer(sys.stdout)
    
    # Write header
    writer.writerow(['Podcast Title', 'DTC Website Link', 'YouTube Link', 'Intro', 'Timestamps'])
    
    # Write data rows
    for podcast in podcasts:
        writer.writerow([
            podcast['title'],
            podcast['dtc_link'],
            podcast['youtube_link'],
            podcast['intro'],
            podcast['timestamps']
        ])


if __name__ == '__main__':
    main()

