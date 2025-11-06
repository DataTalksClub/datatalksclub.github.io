#!/usr/bin/env python3
"""
Generate intros for podcast episodes using OpenAI API.

This script takes a podcast page, finds the timestamp file from podcast-timestamps folder,
and finds the guest's page in _people folder to use their information.

Usage:
    python generate_intro_podcasts.py <podcast_file> [--update] [--api-key YOUR_KEY]
    
Example:
    python generate_intro_podcasts.py _podcast/s01e02-processes.md --update
"""

import os
import sys
import yaml
import argparse
import re
from pathlib import Path
from openai import OpenAI


DEFAULT_PROMPT = """You are an SEO expert creating podcast episode introductions for show notes and homepage descriptions.

TASK: Generate an SEO-optimized intro summary based on episode timestamps and guest information.

INPUT PROVIDED:
1. Episode timestamps showing key topics and discussion flow
2. Guest information (name, title, bio, expertise)

REQUIREMENTS:
- Length: 150-300 words
- Structure: Hook, Guest credibility, Key topics, Value proposition
- SEO: Naturally integrate SEO keywords if they are related to the episode
- Content: Base ONLY on actual timestamps and guest info (no generic filler)

WRITING GUIDELINES:
- Start with the main challenge/question the episode explores
- Establish guest credibility and expertise early
- Highlight 3-4 key topics from timestamps
- End with clear value proposition for listeners
- Use specific, actionable language
- Avoid generic productivity/motivational content
- Don't invent topics not in timestamps

FORMAT STRUCTURE:
1. Opening hook (main challenge/question)
2. Guest introduction with credentials
3. Key topics covered with description of what will be discussed in the episode
4. Learning outcomes and listener benefits
Formated as one coherent and natural text.

TIMESTAMPS:
{timestamps_content}

GUEST INFORMATION:
{guest_info}

OUTPUT: Generate ONLY the intro text using the structure above.
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


def generate_intro(timestamps_content, guest_info, api_key=None):
    """Generate intro using OpenAI API."""
    # Initialize OpenAI client
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        # Will use OPENAI_API_KEY environment variable
        client = OpenAI()
    
    # Format the prompt with all the information
    prompt = DEFAULT_PROMPT.format(
        timestamps_content=timestamps_content,
        guest_info=guest_info
    )
    
    print(f"Prompt size: {len(prompt)} characters")
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
    
    return intro


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
            new_content = f"---\n{new_frontmatter}---{rest_content}"
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
    
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
  
  # Use custom API key
  python generate_intro_podcasts.py _podcast/s01e02-processes.md --api-key sk-...
  
  # Process multiple files
  for file in _podcast/s*.md; do python generate_intro_podcasts.py "$file" --update; done
        """
    )
    
    parser.add_argument('podcast_file', help='Path to the podcast markdown file')
    parser.add_argument('--update', action='store_true', help='Update the file with generated intro')
    parser.add_argument('--api-key', help='OpenAI API key (or set OPENAI_API_KEY env var)')
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
    
    print(f"Processing: {file_path.name}")
    print("-" * 60)
    
    try:
        # Parse the podcast file
        frontmatter, podcast_content, full_content = parse_podcast_file(file_path)
        
        if not frontmatter:
            print("Warning: Could not parse frontmatter from podcast file", file=sys.stderr)
            frontmatter = {}
        
        # Get guest names from front matter
        guests = frontmatter.get('guests', [])
        if not guests:
            print("Warning: No guests found in front matter", file=sys.stderr)
        
        # Get timestamp file
        timestamp_file = get_timestamps_file(file_path)
        if not timestamp_file:
            print(f"Warning: Timestamp file not found: podcast-timestamps/{file_path.stem}.txt", file=sys.stderr)
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
        
        print()
        print("Generating intro...")
        print()
        
        # Generate intro
        intro = generate_intro(timestamps_content, formatted_guest_info, api_key=args.api_key)
        
        print(f"Generated intro ({len(intro)} chars):")
        print(f"  {intro}")
        print()
        
        # Update file if requested
        if args.update:
            if args.dry_run:
                print("\n[DRY RUN] Would update the file with the new intro")
            else:
                success = update_podcast_file(file_path, intro)
                if success:
                    print(f"\n✓ File updated successfully!")
                else:
                    print(f"\n✗ Failed to update file", file=sys.stderr)
                    sys.exit(1)
        else:
            print("\nTo update the file, run with --update flag")
    
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

