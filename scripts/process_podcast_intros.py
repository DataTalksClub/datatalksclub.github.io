#!/usr/bin/env python3
"""
Generate SEO-optimized URL slugs from podcast intro text using OpenAI API.

This script extracts intro text from podcast markdown files and sends it to OpenAI
to generate SEO-optimized URL slugs based on the content.

Usage:
    python process_podcast_intros.py <podcast_file> [--prompt PROMPT] [--api-key YOUR_KEY]
    python process_podcast_intros.py --all-in-dir _podcast/
    python process_podcast_intros.py --file-list podcasts.txt
    
Example:
    python process_podcast_intros.py _podcast/s01e02-processes.md
"""

import os
import sys
import yaml
import argparse
import re
from pathlib import Path
from typing import List, Optional
from openai import OpenAI


DEFAULT_PROMPT = """You are an SEO expert creating SEO-optimized URL slugs.

You are given intro text for a podcast episode.

TASK: Based on the intro text, generate a SEO-optimized URL slug for the podcast episode.

REQUIREMENTS:
- Optimize for SEO with relevant keywords
- Use lowercase letters and hyphens only
- Keep slugs short, clean, and descriptive
- Reflect the main search intent of the episode
- Avoid keyword stuffing or repeating terms
- No dates, stop words (a, the, of, to), or guest names unless essential
- Must map clearly to the episode topic

INTRO TEXT:
{intro_text}

OUTPUT: Generate ONLY the URL slug text.
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


def get_intro_text(podcast_file_path):
    """Extract intro text from a podcast file."""
    frontmatter, _, _ = parse_podcast_file(podcast_file_path)
    
    if not frontmatter:
        return None
    
    intro = frontmatter.get('intro')
    if not intro:
        return None
    
    # Remove HTML breaks for processing
    intro_clean = intro.replace('<br><br>', '\n\n').replace('<br>', '\n')
    return intro_clean.strip()


def send_to_openai(intro_text: str, prompt_template: str, api_key: Optional[str] = None, model: str = "gpt-4o-mini"):
    """Send intro text to OpenAI API with the given prompt."""
    # Initialize OpenAI client
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        # Will use OPENAI_API_KEY environment variable
        client = OpenAI()
    
    # Format the prompt with the intro text
    prompt = prompt_template.format(intro_text=intro_text)
    
    print(f"Sending request to OpenAI (model: {model})...")
    print(f"Intro text length: {len(intro_text)} characters")
    print()
    
    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an SEO expert that generates optimized URL slugs."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        
        result = response.choices[0].message.content.strip()
        return result
    
    except Exception as e:
        print(f"Error calling OpenAI API: {e}", file=sys.stderr)
        raise


def rename_podcast_file(old_path: Path, new_slug: str, dry_run: bool = False) -> Optional[Path]:
    """Rename a podcast file to match the generated slug."""
    # Just strip whitespace and quotes from the slug
    slug = new_slug.strip().strip('"').strip("'")
    
    # Create new filename
    new_filename = f"{slug}.md"
    new_path = old_path.parent / new_filename
    
    # Check if the new file already exists
    if new_path.exists() and new_path != old_path:
        print(f"Warning: Target file already exists: {new_filename}", file=sys.stderr)
        return None
    
    if dry_run:
        print(f"[DRY RUN] Would rename: {old_path.name} -> {new_filename}")
        return new_path
    
    try:
        old_path.rename(new_path)
        print(f"✓ Renamed: {old_path.name} -> {new_filename}")
        return new_path
    except Exception as e:
        print(f"Error renaming file: {e}", file=sys.stderr)
        return None


def get_project_root():
    """Get the project root directory (parent of scripts directory)."""
    script_dir = Path(__file__).parent
    return script_dir.parent


def resolve_podcast_path(podcast_file: str) -> Optional[Path]:
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


def process_podcast_file(
    podcast_file: Path,
    prompt_template: str,
    api_key: Optional[str] = None,
    model: str = "gpt-4o-mini",
    output_file: Optional[Path] = None,
    update: bool = False,
    dry_run: bool = False
) -> bool:
    """Process a single podcast file to extract intro and generate URL slug via OpenAI."""
    print(f"Processing: {podcast_file.name}")
    print("-" * 60)
    
    try:
        # Extract intro text
        intro_text = get_intro_text(podcast_file)
        
        if not intro_text:
            print("Warning: No intro text found in this podcast file", file=sys.stderr)
            return False
        
        print(f"Found intro text ({len(intro_text)} characters):")
        print(f"  {intro_text[:200]}..." if len(intro_text) > 200 else f"  {intro_text}")
        print()
        
        # Send to OpenAI
        result = send_to_openai(intro_text, prompt_template, api_key=api_key, model=model)
        
        print("Generated URL Slug:")
        print("=" * 60)
        print(result)
        print("=" * 60)
        print()
        
        # Save to file if requested
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"✓ Result saved to: {output_file}")
        
        # Rename file if update is requested
        if update:
            new_path = rename_podcast_file(podcast_file, result, dry_run=dry_run)
            if new_path and not dry_run:
                print(f"✓ File renamed successfully")
            elif dry_run:
                print(f"[DRY RUN] File would be renamed")
            else:
                print(f"✗ Failed to rename file", file=sys.stderr)
                return False
        else:
            print("\nTo rename the file, run with --update flag")
        
        return True
    
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Generate SEO-optimized URL slugs from podcast intro text using OpenAI API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate URL slug for a single podcast file
  python process_podcast_intros.py _podcast/s01e02-processes.md
  
  # Generate and automatically rename file
  python process_podcast_intros.py _podcast/s01e02-processes.md --update
  
  # Preview what would be renamed (dry run)
  python process_podcast_intros.py --all-in-dir _podcast/ --update --dry-run
  
  # Process with custom prompt
  python process_podcast_intros.py _podcast/s01e02-processes.md --prompt "Generate a short URL slug: {intro_text}"
  
  # Process multiple files and rename them
  python process_podcast_intros.py _podcast/episode1.md _podcast/episode2.md --update
  
  # Process all files in a directory and rename
  python process_podcast_intros.py --all-in-dir _podcast/ --update
  
  # Read file list from a text file
  python process_podcast_intros.py --file-list podcasts.txt
  
  # Use custom API key
  python process_podcast_intros.py _podcast/s01e02-processes.md --api-key sk-...
  
  # Save output to file
  python process_podcast_intros.py _podcast/s01e02-processes.md --output result.txt
  
  # Use different model
  python process_podcast_intros.py _podcast/s01e02-processes.md --model gpt-4o
        """
    )
    
    parser.add_argument('podcast_files', nargs='*', help='Podcast markdown files to process')
    parser.add_argument('--file-list', help='Text file containing list of podcast files (one per line)')
    parser.add_argument('--all-in-dir', help='Process all .md files in the specified directory')
    parser.add_argument('--prompt', default=DEFAULT_PROMPT, help='Custom prompt template (use {intro_text} as placeholder)')
    parser.add_argument('--api-key', help='OpenAI API key (or set OPENAI_API_KEY env var)')
    parser.add_argument('--model', default='gpt-4o-mini', help='OpenAI model to use (default: gpt-4o-mini)')
    parser.add_argument('--output', help='Output file to save results (only works for single file)')
    parser.add_argument('--update', action='store_true', help='Automatically rename files to match generated slugs')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.podcast_files and not args.file_list and not args.all_in_dir:
        parser.error("Must provide podcast files, --file-list, or --all-in-dir")
    
    # Validate output file (only for single file)
    output_file = None
    if args.output:
        files = get_podcast_files_from_args(args)
        if len(files) > 1:
            parser.error("--output can only be used when processing a single file")
        output_file = Path(args.output)
    
    # Get list of files to process
    files = get_podcast_files_from_args(args)
    
    if not files:
        print("Error: No valid podcast files found", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(files)} podcast file(s) to process")
    if args.dry_run:
        print("[DRY RUN MODE - No changes will be made]")
    if args.update:
        print("[UPDATE MODE - Files will be renamed to match generated slugs]")
    print()
    
    # Use API key from environment if not provided
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("Warning: No API key provided. Set OPENAI_API_KEY env var or use --api-key", file=sys.stderr)
    
    # Process each file
    successful = 0
    failed = 0
    
    for i, podcast_file in enumerate(files, 1):
        print(f"\n[{i}/{len(files)}] ", end='')
        success = process_podcast_file(
            podcast_file,
            prompt_template=args.prompt,
            api_key=api_key,
            model=args.model,
            output_file=output_file if i == 1 else None,  # Only save output for first file
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

