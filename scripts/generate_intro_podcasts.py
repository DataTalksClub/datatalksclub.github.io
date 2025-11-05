#!/usr/bin/env python3
"""
Generate intros for podcast episodes using OpenAI API.

Usage:
    python generate_meta_descriptions.py <podcast_file> [--update] [--api-key YOUR_KEY]
    
Example:
    python generate_meta_descriptions.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md --update
"""

import os
import sys
import yaml
import argparse
from pathlib import Path
from openai import OpenAI


DEFAULT_PROMPT = """You are an SEO expert writing a short intro summary for a podcast episode. This intro will be used as a short description of the episode in the show notes and the homepage.

You are given a file content for a podcast episode. File content includes the title, season, episode, guests, and transcript.

Analyze the file content below carefully and generate an SEO-optimized intro summary, one paragraph starting with “In this episode…”:
- Add one clear sentence stating the main challenge or question the episode explores.
- Follow with one sentence summarizing what listeners will gain or learn.
- Naturally include the primary keyword and 1–2 related keywords.
- Briefly describe what the guest discusses in the transcript: focus on key topics, insights, and takeaways, not filler conversation.
- Use the guest’s title and company as of the podcast recording (ignore later updates).
- Exclude any mention of recent career changes or details unrelated to the episode’s timeframe.

IMPORTANT: Base the intro ONLY on the actual topics discussed in the file content. Do NOT make up generic productivity/motivational content.
FILE CONTENT:
{file_content}

Generate ONLY the meta description text. Use specific topics from the file content above.
"""


def parse_podcast_file(file_path):
    """Parse a podcast markdown file and extract content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def generate_meta_description(file_content, api_key=None):
    """Generate meta description using OpenAI API."""
    # Initialize OpenAI client
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        # Will use OPENAI_API_KEY environment variable
        client = OpenAI()
    
    # Format the prompt with the file content
    prompt = DEFAULT_PROMPT.format(file_content=file_content)
    
    # Call OpenAI API
    response = client.responses.create(
        model="gpt-5-nano",  # Using gpt-5-nano
        input=prompt,
    )
    
    meta_description = response.output_text.strip()
    
    # Remove quotes if present
    if meta_description.startswith('"') and meta_description.endswith('"'):
        meta_description = meta_description[1:-1]
    if meta_description.startswith("'") and meta_description.endswith("'"):
        meta_description = meta_description[1:-1]
    
    return meta_description


def update_podcast_file(file_path, meta_description):
    """Update the podcast file with the generated meta description."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the frontmatter section
    if content.startswith('---\n'):
        import re
        # Find the closing ---
        match = re.search(r'\n---\n', content[4:])
        if match:
            end_pos = match.start() + 4
            frontmatter_text = content[4:end_pos]
            rest_content = content[end_pos + 5:]
            
            # Parse frontmatter
            frontmatter = yaml.safe_load(frontmatter_text)
            
            # Add or update description field
            frontmatter['description'] = meta_description
            
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
        description='Generate meta descriptions for podcast episodes using OpenAI API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate description and display it
  python generate_meta_descriptions.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md
  
  # Generate and update the file
  python generate_meta_descriptions.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md --update
  
  # Use custom API key
  python generate_meta_descriptions.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md --api-key sk-...
  
  # Process multiple files
  for file in _podcast/s22e*.md; do python generate_meta_descriptions.py "$file" --update; done
        """
    )
    
    parser.add_argument('podcast_file', help='Path to the podcast markdown file')
    parser.add_argument('--update', action='store_true', help='Update the file with generated description')
    parser.add_argument('--api-key', help='OpenAI API key (or set OPENAI_API_KEY env var)')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    # Check if file exists
    file_path = Path(args.podcast_file)
    if not file_path.exists():
        print(f"Error: File not found: {args.podcast_file}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing: {file_path.name}")
    print("-" * 60)
    
    try:
        # Read the file content
        file_content = parse_podcast_file(file_path)
        
        print(f"File size: {len(file_content)} characters")
        print(f"Content preview (first 200 chars):")
        print(f"  {file_content[:200]}...")
        print()
        
        # Generate new description
        print("Generating meta description...")
        
        meta_description = generate_meta_description(file_content, api_key=args.api_key)
        
        print(f"\nGenerated description ({len(meta_description)} chars):")
        print(f"  {meta_description}")
        print()
        
        # Check length
        if len(meta_description) > 160:
            print(f"⚠️  WARNING: Description is {len(meta_description)} chars (recommended: 140-155, max: 160)")
        elif len(meta_description) < 140:
            print(f"ℹ️  INFO: Description is {len(meta_description)} chars (recommended: 140-155)")
        else:
            print(f"✓ Description length is optimal: {len(meta_description)} chars")
        
        # Update file if requested
        if args.update:
            if args.dry_run:
                print("\n[DRY RUN] Would update the file with the new description")
            else:
                success = update_podcast_file(file_path, meta_description)
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

