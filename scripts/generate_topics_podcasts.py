#!/usr/bin/env python3
"""
Generate topics for podcast episodes using OpenAI API.

This script takes a podcast page, extracts quotableClips from the frontmatter,
and generates relevant topics based on the episode content.

Usage:
    python generate_topics_podcasts.py <podcast_file> [--update] [--api-key YOUR_KEY]
    python generate_topics_podcasts.py --all-in-dir _podcast/ --update
    python generate_topics_podcasts.py --file-list podcasts.txt --update
    
Example:
    python generate_topics_podcasts.py _podcast/s01e02-processes.md --update
"""

import os
import sys
import argparse
import yaml
import re
from pathlib import Path
from typing import List
from openai import OpenAI


# Standard topic list - curated from existing podcasts
DEFAULT_TOPIC_LIST = [
    "machine learning",
    "MLOps",
    "data engineering",
    "data science",
    "AI",
    "LLMs",
    "career growth",
    "career transition",
    "leadership",
    "freelance",
    "tools",
    "open-source",
    "startups",
    "production",
    "team building",
    "data governance",
    "software engineering",
    "entrepreneurship",
    "job search",
    "data analytics",
    "data strategy",
    "product management",
    "communication",
    "practices",
    "bioinformatics",
    "computer vision",
    "NLP",
    "consulting",
    "remote work",
    "career development",
]


def load_topic_list():
    """Load topic list from file if it exists, otherwise use default."""
    script_dir = Path(__file__).parent
    topics_file = script_dir / 'topic_list.txt'
    
    if topics_file.exists():
        try:
            with open(topics_file, 'r', encoding='utf-8') as f:
                topics = [line.strip() for line in f if line.strip()]
            print(f"Loaded {len(topics)} topics from {topics_file.name}")
            return topics
        except Exception as e:
            print(f"Warning: Could not load topic list from file: {e}")
            return DEFAULT_TOPIC_LIST
    else:
        return DEFAULT_TOPIC_LIST


# Load topic list (will use file if exists, otherwise default)
TOPIC_LIST = load_topic_list()


DEFAULT_PROMPT = """You are an expert at categorizing technical podcast content based on topics.

You are given episode quotable clips showing key topics and discussion flow from a podcast episode.

TASK: Based on the podcast quotable clips, select 3-5 most relevant topics from the provided topic list.

AVAILABLE TOPICS:
{topic_list}

REQUIREMENTS:
- You MUST choose topics from the available topics list OR generate new topics that are relevant to the episode content and are of the similar level of specificity as the available topics.
- Select between 3 to 5 topics that best represent the episode content
- Choose topics that are most prominently discussed in the quotable clips
- Prioritize specific technical topics over general career topics when both are present
- If the episode clearly focuses on a technology/practice, include that
- If career journey or transition is a significant theme, include relevant career topics
- Consider both the depth and breadth of coverage when selecting topics

QUOTABLE CLIPS:
{clips_content}

OUTPUT FORMAT: Return ONLY a valid YAML list of topics, nothing else.
Example format:
- machine learning
- MLOps
- career transition
- leadership
- tools
"""


def get_quotable_clips(podcast_file_path):
    """Extract quotableClips from podcast frontmatter."""
    with open(podcast_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    
    try:
        frontmatter_data = yaml.safe_load(match.group(1))
        clips = frontmatter_data.get('quotableClips', [])
        
        if not clips:
            return None
        
        # Format clips as text
        clips_text = []
        for clip in clips:
            name = clip.get('name', '')
            # Convert startOffset (seconds) to timestamp format
            start_seconds = clip.get('startOffset', 0)
            hours = start_seconds // 3600
            minutes = (start_seconds % 3600) // 60
            seconds = start_seconds % 60
            timestamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            clips_text.append(f"{timestamp} {name}")
        
        return '\n'.join(clips_text)
    
    except Exception as e:
        print(f"Error parsing frontmatter: {e}")
        return None


def generate_topics(clips_content, api_key=None):
    """Generate topics using OpenAI API."""
    # Initialize OpenAI client
    if api_key:
        client = OpenAI(api_key=api_key)
    else:
        # Will use OPENAI_API_KEY environment variable
        client = OpenAI()
    
    # Format the topic list for the prompt
    topic_list_formatted = '\n'.join([f"- {topic}" for topic in TOPIC_LIST])
    
    # Format the prompt with all the information
    prompt = DEFAULT_PROMPT.format(
        topic_list=topic_list_formatted,
        clips_content=clips_content,
    )

    print(f"Prompt size: {len(prompt)} characters")
    print(f"  - Clips: {len(clips_content)} characters")
    print(f"  - Available topics: {len(TOPIC_LIST)}")
    print()
    
    # Call OpenAI API
    response = client.responses.create(
        model="gpt-5-mini",  # Using gpt-5-mini
        input=prompt,
    )
    
    topics_yaml = response.output_text.strip()
    
    # Remove markdown code blocks if present
    topics_yaml = re.sub(r'^```ya?ml\s*\n', '', topics_yaml)
    topics_yaml = re.sub(r'\n```\s*$', '', topics_yaml)
    
    # Parse the YAML to get list of topics
    try:
        topics = yaml.safe_load(topics_yaml)
        if not isinstance(topics, list):
            raise ValueError("Response is not a list")
        
        # Process and validate topics
        valid_topics = []
        new_topics = []
        
        for topic in topics:
            # Normalize and check
            topic_clean = topic.strip()
            
            if topic_clean in TOPIC_LIST:
                valid_topics.append(topic_clean)
            else:
                # New topic - accept it if it's reasonable
                print(f"  New topic found: '{topic_clean}'")
                valid_topics.append(topic_clean)
                new_topics.append(topic_clean)
        
        return valid_topics, new_topics
    except Exception as e:
        print(f"Error parsing topics: {e}")
        print(f"Raw response:\n{topics_yaml}")
        return [], []


def update_podcast_file(file_path, topics):
    """Update the podcast file with the generated topics."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse frontmatter
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        print("Error: Could not find frontmatter")
        return False
    
    frontmatter_str = match.group(1)
    body = content[match.end():]
    
    # Parse YAML frontmatter
    try:
        frontmatter_data = yaml.safe_load(frontmatter_str)
    except Exception as e:
        print(f"Error parsing frontmatter YAML: {e}")
        return False
    
    # Update or add topics field
    frontmatter_data['topics'] = topics
    
    # Rebuild the file content
    # We need to maintain formatting, so we'll find the right place to insert/update topics
    lines = frontmatter_str.split('\n')
    
    # Find if topics already exists
    topics_line_idx = None
    topics_end_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith('topics:'):
            topics_line_idx = i
            # Find the end of topics list
            for j in range(i + 1, len(lines)):
                if lines[j] and not lines[j].startswith('-') and not lines[j].startswith(' '):
                    topics_end_idx = j
                    break
            else:
                topics_end_idx = len(lines)
            break
    
    # Format topics as YAML list
    topics_yaml_lines = ['topics:']
    for topic in topics:
        topics_yaml_lines.append(f'- {topic}')
    
    # Insert or replace topics
    if topics_line_idx is not None:
        # Replace existing topics
        new_lines = lines[:topics_line_idx] + topics_yaml_lines + lines[topics_end_idx:]
    else:
        # Find a good place to insert (after description or intro if they exist)
        insert_idx = len(lines)
        for i, line in enumerate(lines):
            if line.strip().startswith('dateadded:'):
                insert_idx = i
                break
            elif line.strip().startswith('description:'):
                insert_idx = i + 1
                break
            elif line.strip().startswith('intro:'):
                # Skip multiline intro
                for j in range(i + 1, len(lines)):
                    if lines[j] and not lines[j].startswith(' ') and ':' in lines[j]:
                        insert_idx = j
                        break
                break
        
        new_lines = lines[:insert_idx] + topics_yaml_lines + lines[insert_idx:]
    
    # Reconstruct content
    new_frontmatter = '\n'.join(new_lines)
    new_content = f"---\n{new_frontmatter}\n---{body}"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
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
        # Exclude template file
        files = [f for f in files if f.name != '_template.md']
    
    else:
        # From command line arguments
        for podcast_file in args.podcast_files:
            file_path = resolve_podcast_path(podcast_file)
            if file_path:
                files.append(file_path)
            else:
                print(f"Error: File not found: {podcast_file}", file=sys.stderr)
    
    return files


def check_existing_topics(podcast_file: Path) -> bool:
    """Check if podcast already has topics."""
    with open(podcast_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        try:
            frontmatter_data = yaml.safe_load(match.group(1))
            topics = frontmatter_data.get('topics', [])
            return bool(topics)
        except:
            pass
    
    return False


def process_podcast_file(podcast_file: Path, api_key: str = None, update: bool = False, 
                         dry_run: bool = False, skip_existing: bool = False) -> tuple:
    """Process a single podcast file to generate and optionally update topics.
    
    Returns:
        tuple: (success: bool, new_topics: list)
    """
    print(f"Processing: {podcast_file.name}")
    print("-" * 60)
    
    try:
        # Check if already has topics
        if skip_existing and check_existing_topics(podcast_file):
            print(f"Skipping: Already has topics")
            print()
            return True, []
        
        # Get quotable clips from frontmatter
        clips_content = get_quotable_clips(podcast_file)
        if not clips_content:
            print(f"Warning: No quotableClips found in frontmatter", file=sys.stderr)
            print(f"Skipping this file.")
            print()
            return True, []
        
        print(f"Found {len(clips_content.splitlines())} quotable clips")
        print()
        print("Generating topics...")
        print()
        
        # Generate topics
        topics, new_topics = generate_topics(clips_content, api_key=api_key)
        
        if not topics:
            print("Error: No valid topics generated")
            return False, []
        
        print(f"Generated {len(topics)} topics:")
        for topic in topics:
            print(f"  - {topic}")
        print()
        
        # Update file if requested
        if update:
            if dry_run:
                print("\n[DRY RUN] Would update the file with these topics")
                return True, new_topics
            else:
                success = update_podcast_file(podcast_file, topics)
                if success:
                    print(f"\n✓ File updated successfully!")
                    return True, new_topics
                else:
                    print(f"\n✗ Failed to update file", file=sys.stderr)
                    return False, []
        else:
            print("\nTo update the file, run with --update flag")
            return True, new_topics
    
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return False, []


def main():
    parser = argparse.ArgumentParser(
        description='Generate topics for podcast episodes using OpenAI API based on quotableClips',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate topics and display them
  python generate_topics_podcasts.py _podcast/building-ml-platform.md
  
  # Generate and update the file
  python generate_topics_podcasts.py _podcast/building-ml-platform.md --update
  
  # Process multiple files
  python generate_topics_podcasts.py _podcast/episode1.md _podcast/episode2.md --update
  
  # Process all files in a directory (skip those with existing topics)
  python generate_topics_podcasts.py --all-in-dir _podcast/ --update --skip-existing
  
  # Read file list from a text file
  python generate_topics_podcasts.py --file-list podcasts_without_topics.txt --update
  
  # Use custom API key
  python generate_topics_podcasts.py _podcast/building-ml-platform.md --api-key sk-...
  
  # Dry run to see what would be done
  python generate_topics_podcasts.py --all-in-dir _podcast/ --dry-run

Note: This script reads quotableClips from the podcast frontmatter. 
      Files without quotableClips will be skipped.
        """
    )
    
    parser.add_argument('podcast_files', nargs='*', help='Podcast markdown files to process')
    parser.add_argument('--file-list', help='Text file containing list of podcast files (one per line)')
    parser.add_argument('--all-in-dir', help='Process all .md files in the specified directory')
    parser.add_argument('--update', action='store_true', help='Update the file with generated topics')
    parser.add_argument('--skip-existing', action='store_true', help='Skip files that already have topics')
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
    if args.skip_existing:
        print("[Skipping files with existing topics]")
    if args.dry_run:
        print("[DRY RUN MODE - No changes will be made]")
    print()
    
    # Use API key from environment if not provided
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')
    
    # Process each file
    successful = 0
    failed = 0
    all_new_topics = []
    
    for i, podcast_file in enumerate(files, 1):
        print(f"\n[{i}/{len(files)}] ", end='')
        success, new_topics = process_podcast_file(
            podcast_file,
            api_key=api_key,
            update=args.update,
            dry_run=args.dry_run,
            skip_existing=args.skip_existing
        )
        
        if success:
            successful += 1
            if new_topics:
                all_new_topics.extend(new_topics)
        else:
            failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"Summary: {successful} successful, {failed} failed")
    
    # Report new topics found
    if all_new_topics:
        unique_new_topics = sorted(set(all_new_topics))
        print(f"\n🆕 Found {len(unique_new_topics)} new topics:")
        for topic in unique_new_topics:
            print(f"  - {topic}")
        
        # Update the topic list file
        script_dir = Path(__file__).parent
        topics_file = script_dir / 'topic_list.txt'
        
        # Read existing topics
        existing_topics = list(TOPIC_LIST)
        
        # Add new topics
        for topic in unique_new_topics:
            if topic not in existing_topics:
                existing_topics.append(topic)
        
        # Save updated list
        existing_topics.sort()
        with open(topics_file, 'w', encoding='utf-8') as f:
            for topic in existing_topics:
                f.write(f"{topic}\n")
        
        print(f"\n✓ Updated topic list saved to: {topics_file}")
        print(f"  Total topics: {len(existing_topics)} (was {len(TOPIC_LIST)})")
        print(f"\nTo use the updated list, update TOPIC_LIST in generate_topics_podcasts.py")
    
    if failed > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()

