#!/usr/bin/env python3
"""
Generate intros for podcast episodes using OpenAI API.

This script takes a podcast page, finds the timestamp file from podcast-timestamps folder,
and finds the guest's page in _people folder to use their information.

Usage:
    python generate_intro_podcasts.py <podcast_file> [--update] [--api-key YOUR_KEY]
    python generate_intro_podcasts.py --all-in-dir _podcast/ --update
    python generate_intro_podcasts.py --file-list podcasts.txt --update
    
Example:
    python generate_intro_podcasts.py _podcast/s01e02-processes.md --update
"""

import os
import sys
import yaml
import argparse
import re
from pathlib import Path
from typing import List
from openai import OpenAI


DEFAULT_PROMPT = """You are an SEO expert creating podcast episode introductions for show notes and homepage descriptions.

You are given episode timestamps showing key topics and discussion flow and guest information (name, title, bio, expertise) and episode title.

TASK: Generate an SEO-optimized intro summary based on episode timestamps, guest information and episode title.

REQUIREMENTS:
- Length: 150-200 words
- Prioritize the topic highlighted in the episode title when generating the intro
- Should include opening hook with a main challenge/question the episode explores, guest credibility for Google's E-E-A-T, introduce the key topics, and provide a value proposition for the listener
- No marketer talk and hype, just focus on the content of the episode and the value it provides to the 
- Do not invent things that are not in the timestamps or the episode title
- Naturally integrate SEO keywords if they are related to the episode

EPISODE TITLE:
{episode_title}

TIMESTAMPS:
{timestamps_content}

GUEST INFORMATION:
{guest_info}

OUTPUT: Generate ONLY the intro text.
"""


def parse_podcast_file(file_path):
    """Parse a podcast markdown file and extract front matter and content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract front matter
    if content.startswith('---\n'):
        match = re.search(r'\n---\n', content[4:])
        if match:
            end_pos = match.start() + 4
            frontmatter_text = content[4:end_pos]
            rest_content = content[end_pos + 5:]
            
            try:
                frontmatter = yaml.safe_load(frontmatter_text)
                return frontmatter, rest_content, content
            except yaml.YAMLError:
                return None, content, content
    
    # No frontmatter found
    return None, content, content


def get_timestamps_file(podcast_file_path):
    """Get the timestamp file path for a podcast."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    timestamps_dir = project_root / 'podcast-timestamps'
    
    # Use podcast filename (without .md) for the timestamp file
    podcast_name = podcast_file_path.stem  # filename without extension
    timestamp_file = timestamps_dir / f"{podcast_name}.txt"
    
    return timestamp_file if timestamp_file.exists() else None


def get_guest_info(guest_short):
    """Get guest information from _people folder."""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    people_dir = project_root / '_people'
    
    guest_file = people_dir / f"{guest_short}.md"
    
    if not guest_file.exists():
        return None
    
    with open(guest_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract front matter
    if content.startswith('---\n'):
        match = re.search(r'\n---\n', content[4:])
        if match:
            end_pos = match.start() + 4
            frontmatter_text = content[4:end_pos]
            rest_content = content[end_pos + 5:].strip()
            
            try:
                frontmatter = yaml.safe_load(frontmatter_text)
                # Combine front matter info with bio content
                guest_info = {
                    'name': frontmatter.get('title', ''),
                    'short': frontmatter.get('short', ''),
                    'picture': frontmatter.get('picture', ''),
                    'linkedin': frontmatter.get('linkedin', ''),
                    'twitter': frontmatter.get('twitter', ''),
                    'web': frontmatter.get('web', ''),
                    'bio': rest_content
                }
                return guest_info
            except yaml.YAMLError:
                return None
    
    return None


def format_guest_info(guests_info):
    """Format guest information for the prompt."""
    if not guests_info:
        return "No guest information available."
    
    formatted = []
    for guest in guests_info:
        if guest:
            info_parts = []
            if guest.get('name'):
                info_parts.append(f"Name: {guest['name']}")
            if guest.get('bio'):
                info_parts.append(f"Bio: {guest['bio']}")
            if guest.get('linkedin'):
                info_parts.append(f"LinkedIn: {guest['linkedin']}")
            if guest.get('twitter'):
                info_parts.append(f"Twitter: {guest['twitter']}")
            if guest.get('web'):
                info_parts.append(f"Website: {guest['web']}")
            
            formatted.append("\n".join(info_parts))
    
    return "\n\n".join(formatted) if formatted else "No guest information available."


def generate_intro(timestamps_content, guest_info, episode_title=None, api_key=None):
    """Generate intro using OpenAI API."""
    # Initialize OpenAI client
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        # Will use OPENAI_API_KEY environment variable
        client = OpenAI()
    
    # Format the prompt with all the information
    prompt = DEFAULT_PROMPT.format(
        episode_title=episode_title or "No episode title available",
        timestamps_content=timestamps_content,
        guest_info=guest_info
    )
    
    print(f"Prompt size: {len(prompt)} characters")
    print(f"  - Episode title: {len(episode_title or '')} characters")
    print(f"  - Timestamps: {len(timestamps_content)} characters")
    print(f"  - Guest info: {len(guest_info)} characters")
    print()
    
    # Call OpenAI API
    response = client.responses.create(
        model="gpt-5-mini",  # Using gpt-5-nano
        input=prompt,
    )
    
    intro = response.output_text.strip()
    
    # Remove quotes if present
    if intro.startswith('"') and intro.endswith('"'):
        intro = intro[1:-1]
    if intro.startswith("'") and intro.endswith("'"):
        intro = intro[1:-1]
    
    # Format intro: replace paragraph breaks with <br><br>
    intro = format_intro_with_breaks(intro)
    
    return intro


def format_intro_with_breaks(intro):
    """Format intro text by replacing paragraph breaks with <br><br>."""
    # Split by double newlines (paragraph breaks)
    paragraphs = []
    for para in intro.split('\n\n'):
        para = para.strip()
        if para:
            # Replace single newlines within paragraph with spaces
            para = ' '.join(para.split('\n'))
            paragraphs.append(para)
    
    # Join paragraphs with <br><br>
    formatted_intro = ' <br><br> '.join(paragraphs)
    
    return formatted_intro


def update_podcast_file(file_path, intro):
    """Update the podcast file with the generated intro."""
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
            
            # Add or update intro field
            frontmatter['intro'] = intro
            
            # Convert back to YAML
            new_frontmatter = yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False)
            
            # Reconstruct file
            new_content = f"---\n{new_frontmatter}---\n{rest_content}"
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
    
    return False


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
    """Process a single podcast file to generate and optionally update the intro."""
    print(f"Processing: {podcast_file.name}")
    print("-" * 60)
    
    try:
        # Parse the podcast file
        frontmatter, podcast_content, full_content = parse_podcast_file(podcast_file)
        
        if not frontmatter:
            print("Warning: Could not parse frontmatter from podcast file", file=sys.stderr)
            frontmatter = {}
        
        # Get guest names from front matter
        guests = frontmatter.get('guests', [])
        if not guests:
            print("Warning: No guests found in front matter", file=sys.stderr)
        
        # Get timestamp file
        timestamp_file = get_timestamps_file(podcast_file)
        if not timestamp_file:
            print(f"Warning: Timestamp file not found: podcast-timestamps/{podcast_file.stem}.txt", file=sys.stderr)
            timestamps_content = "No timestamps available."
        else:
            print(f"Found timestamps: {timestamp_file.relative_to(timestamp_file.parent.parent)}")
            with open(timestamp_file, 'r', encoding='utf-8') as f:
                timestamps_content = f.read().strip()
        
        # Get guest information
        guests_info = []
        for guest_short in guests:
            guest_info = get_guest_info(guest_short)
            if guest_info:
                print(f"Found guest info: {guest_short}")
                guests_info.append(guest_info)
            else:
                print(f"Warning: Guest info not found for: {guest_short}", file=sys.stderr)
        
        formatted_guest_info = format_guest_info(guests_info)
        
        # Get episode title from frontmatter
        episode_title = frontmatter.get('title', '')
        
        print()
        print("Generating intro...")
        print()
        
        # Generate intro
        intro = generate_intro(timestamps_content, formatted_guest_info, episode_title=episode_title, api_key=api_key)
        
        print(f"Generated intro ({len(intro)} chars):")
        print(f"  {intro}")
        print()
        
        # Update file if requested
        if update:
            if dry_run:
                print("\n[DRY RUN] Would update the file with the new intro")
                return True
            else:
                success = update_podcast_file(podcast_file, intro)
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
        description='Generate intros for podcast episodes using OpenAI API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate intro and display it
  python generate_intro_podcasts.py _podcast/s01e02-processes.md
  
  # Generate and update the file
  python generate_intro_podcasts.py _podcast/s01e02-processes.md --update
  
  # Process multiple files
  python generate_intro_podcasts.py _podcast/episode1.md _podcast/episode2.md --update
  
  # Process all files in a directory
  python generate_intro_podcasts.py --all-in-dir _podcast/ --update
  
  # Read file list from a text file
  python generate_intro_podcasts.py --file-list podcasts.txt --update
  
  # Use custom API key
  python generate_intro_podcasts.py _podcast/s01e02-processes.md --api-key sk-...
  
  # Dry run to see what would be done
  python generate_intro_podcasts.py --all-in-dir _podcast/ --dry-run
        """
    )
    
    parser.add_argument('podcast_files', nargs='*', help='Podcast markdown files to process')
    parser.add_argument('--file-list', help='Text file containing list of podcast files (one per line)')
    parser.add_argument('--all-in-dir', help='Process all .md files in the specified directory')
    parser.add_argument('--update', action='store_true', help='Update the file with generated intro')
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

