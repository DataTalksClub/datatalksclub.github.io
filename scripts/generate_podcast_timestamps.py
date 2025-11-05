#!/usr/bin/env python3
"""
Generate timestamps for podcast episodes using OpenAI API.

Automatically saves timestamps to podcast-timestamps/<podcast-name>.txt

Usage:
    python generate_podcast_timestamps.py <podcast_file> [--api-key YOUR_KEY]
    
Example:
    python generate_podcast_timestamps.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md
    # Creates: podcast-timestamps/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.txt
    
Note: To insert generated timestamps into the transcript, use insert_podcast_timestamps.py
"""

import os
import sys
import yaml
import argparse
from pathlib import Path
from openai import OpenAI


DEFAULT_PROMPT = """You are an expert creating timestamps for a podcast episode.

You are given file content for a podcast episode including title, season, episode, guests, and transcript.

TASK: Generate new high-quality timestamps that accurately reflect the content and help listeners navigate the episode.

REQUIREMENTS:
- Max 30 timestamps
- Create a structured outline highlighting major topics
- Be factual and accurate
- Do not be over-granular
- Use concise, nominative phrases (describe what's covered, not what's asked)
- Focus on clarity, parallel grammar, and information hierarchy
- Naturally include key SEO keywords to timestamps if they are related to timestamps and accurately reflect the content of a given timestamp.
- Do not repeat existing timestamps mentioned as "header" in the transcript. Generate new, high-quality timestamps that are valuable to the listener for navigating the episode.
- Don't write: "How to contribute to open source?"
- Do write: "Open Source Contribution: Starting Small & Building Confidence."

Format as: HH:MM:SS Topic

Example:
00:00:00 Podcast Introduction
00:01:20 Introduction: CEO Chris Bergh and DataOps Origin Story
00:01:50 Career Shift: Managing Data Teams; Realizing Process Problems
00:04:15 Concept: Data as a Factory; Agile Software & Hard Hats
00:06:42 DataOps Essence: Lowering Errors; Cycle Time; Productivity
00:13:20 Naming DataOps; DevOps Analogy; Stressful Data Work
00:21:02 Defining "Done" and "Good"; Balance: Heroism vs. Fear
00:28:14 Lean Principles; Two Iteration Cycles; Avoiding Silos
00:34:37 Tool: Seven Steps to DataOps; Automate Checklists
00:38:01 Career Goal: Replaceability; Avoiding the Technical Hairball
00:44:12 DataOps Adoption Challenges; 15% Time for Process
00:51:15 Concept: DataOps vs. MLOps (Same Principles Applied)
00:56:32 Grilling at Data Kitchen: Automating Environments and Orchestration
00:56:40 DataKitchen Platform: Automating Environments and Orchestration
01:00:27 The DataOps Cookbook: Free Resources for Learning and Adopting DataOps
01:01:48 Resources: DataOps Cookbook, Manifesto, and Manager Book

Do not include speaker names or questions unless essential to the context.

FILE CONTENT:
{file_content}

Generate ONLY the timestamps text. Use specific topics from the file content above.
"""


def parse_podcast_file(file_path):
    """Parse a podcast markdown file and extract content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def generate_podcast_timestamps(file_content, api_key=None):
    """Generate podcast timestamps using OpenAI API."""
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
        model="gpt-5-mini",  # Using gpt-5-mini
        input=prompt,
    )
    
    meta_description = response.output_text.strip()
    
    # Remove quotes if present
    if meta_description.startswith('"') and meta_description.endswith('"'):
        meta_description = meta_description[1:-1]
    if meta_description.startswith("'") and meta_description.endswith("'"):
        meta_description = meta_description[1:-1]
    
    return meta_description


def main():
    parser = argparse.ArgumentParser(
        description='Generate timestamps for podcast episodes using OpenAI API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate timestamps (saved to podcast-timestamps/ automatically)
  python generate_podcast_timestamps.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md
  
  # Use custom API key
  python generate_podcast_timestamps.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md --api-key sk-...
  
  # Then insert timestamps using the separate script
  python insert_podcast_timestamps.py _podcast/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.md --timestamps-file podcast-timestamps/s22e04-how-to-build-and-evaluate-ai-systems-in-age-of-llms.txt --update
        """
    )
    
    parser.add_argument('podcast_file', help='Path to the podcast markdown file')
    parser.add_argument('--api-key', help='OpenAI API key (or set OPENAI_API_KEY env var)')
    
    args = parser.parse_args()
    
    # Resolve file path - try relative to current dir, then relative to project root
    file_path = Path(args.podcast_file)
    if not file_path.exists():
        # If not found, try relative to project root (where script is located)
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        file_path = project_root / args.podcast_file
    
    if not file_path.exists():
        print(f"Error: File not found: {args.podcast_file}", file=sys.stderr)
        print(f"  Tried: {Path(args.podcast_file).resolve()}", file=sys.stderr)
        print(f"  Tried: {(Path(__file__).parent.parent / args.podcast_file).resolve()}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing: {file_path.name}", file=sys.stderr)
    print("-" * 60, file=sys.stderr)
    
    try:
        # Read the file content
        file_content = parse_podcast_file(file_path)
        
        print(f"File size: {len(file_content)} characters", file=sys.stderr)
        print("Generating timestamps using AI...", file=sys.stderr)
        print(file=sys.stderr)
        
        # Generate timestamps
        timestamps = generate_podcast_timestamps(file_content, api_key=args.api_key)
        
        # Create output file path
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        timestamps_dir = project_root / 'podcast-timestamps'
        timestamps_dir.mkdir(exist_ok=True)
        
        # Use podcast filename (without .md) for the timestamp file
        podcast_name = file_path.stem  # filename without extension
        output_file = timestamps_dir / f"{podcast_name}.txt"
        
        # Write timestamps to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(timestamps)
        
        # Output to stdout as well (for backward compatibility)
        print(timestamps)
        
        # Instructions to stderr
        print(file=sys.stderr)
        print("=" * 60, file=sys.stderr)
        print(f"✓ Timestamps saved to: {output_file.relative_to(project_root)}", file=sys.stderr)
        print(file=sys.stderr)
        print("Next steps:", file=sys.stderr)
        print("1. Review the timestamps file", file=sys.stderr)
        print("2. Edit if needed", file=sys.stderr)
        print("3. Insert into transcript:", file=sys.stderr)
        print(f"   python insert_podcast_timestamps.py {args.podcast_file} --timestamps-file {output_file.relative_to(project_root)} --update", file=sys.stderr)
    
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

