#!/usr/bin/env python3
"""
Script to add 'context' field to podcast episodes by copying the 'title' field.
Processes all markdown files in _podcast/to-update directory.
Inserts the 'context' field right after the 'title' field.
"""

import os
import re
from pathlib import Path


def extract_yaml_and_content(file_content):
    """
    Extract YAML front matter and remaining content from a markdown file.
    
    Returns:
        tuple: (yaml_lines, remaining_content)
    """
    # Match YAML front matter between --- delimiters
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, file_content, re.DOTALL)
    
    if not match:
        raise ValueError("No YAML front matter found")
    
    yaml_content = match.group(1)
    remaining_content = match.group(2)
    
    # Split YAML into lines
    yaml_lines = yaml_content.split('\n')
    
    return yaml_lines, remaining_content


def rebuild_file(yaml_lines, remaining_content):
    """
    Rebuild the markdown file with updated YAML front matter.
    
    Args:
        yaml_lines: List of YAML lines
        remaining_content: Content after YAML front matter
        
    Returns:
        str: Complete file content
    """
    yaml_str = '\n'.join(yaml_lines)
    return f"---\n{yaml_str}\n---\n{remaining_content}"


def find_title_lines(yaml_lines):
    """
    Find the line indices where the title field starts and ends.
    
    Returns:
        tuple: (start_index, end_index) or (None, None) if not found
    """
    title_start = None
    title_end = None
    
    i = 0
    while i < len(yaml_lines):
        line = yaml_lines[i]
        
        # Check if this line starts with "title:"
        if line.startswith('title:'):
            title_start = i
            
            # Find where the title value ends (check if it's multi-line)
            # Multi-line values are indented
            j = i + 1
            while j < len(yaml_lines):
                next_line = yaml_lines[j]
                # If the next line starts with a space/tab, it's part of the title
                # If it starts with a letter/number (new field), title ends
                if next_line and not next_line[0].isspace() and next_line[0] != '-':
                    title_end = j - 1
                    break
                j += 1
            
            # If we reached the end without finding a new field
            if title_end is None:
                title_end = len(yaml_lines) - 1
            
            return title_start, title_end
        
        i += 1
    
    return None, None


def extract_title_value(yaml_lines, start_idx, end_idx):
    """
    Extract the complete title value from the YAML lines.
    
    Returns:
        str: The complete title value
    """
    if start_idx is None:
        return None
    
    # Get the title lines
    title_lines = yaml_lines[start_idx:end_idx + 1]
    
    # Join them back together
    return '\n'.join(title_lines)


def process_episode(file_path):
    """
    Process a single episode file: add 'context' field from 'title' if it doesn't exist.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        bool: True if file was modified, False otherwise
    """
    print(f"Processing: {file_path.name}")
    
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML and content
    try:
        yaml_lines, remaining_content = extract_yaml_and_content(content)
    except Exception as e:
        print(f"  ⚠️  Error parsing {file_path.name}: {e}")
        return False
    
    # Check if context field already exists
    has_context = any(line.startswith('context:') for line in yaml_lines)
    if has_context:
        print(f"  ℹ️  Already has 'context' field, skipping")
        return False
    
    # Find title field
    title_start, title_end = find_title_lines(yaml_lines)
    if title_start is None:
        print(f"  ⚠️  No 'title' field found, skipping")
        return False
    
    # Extract title value
    title_section = extract_title_value(yaml_lines, title_start, title_end)
    
    # Create context field by replacing "title:" with "context:"
    context_section = title_section.replace('title:', 'context:', 1)
    context_lines = context_section.split('\n')
    
    # Insert context lines right after the title section
    insert_position = title_end + 1
    for i, context_line in enumerate(context_lines):
        yaml_lines.insert(insert_position + i, context_line)
    
    # Rebuild file
    new_content = rebuild_file(yaml_lines, remaining_content)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  ✅ Added 'context' field")
    return True


def main():
    """Main function to process all episodes in to-update directory."""
    # Get the script directory and navigate to podcast directory
    script_dir = Path(__file__).parent
    podcast_dir = script_dir.parent / '_podcast' / 'to-update'
    
    if not podcast_dir.exists():
        print(f"❌ Directory not found: {podcast_dir}")
        return
    
    print(f"Processing episodes in: {podcast_dir}\n")
    
    # Get all markdown files
    md_files = sorted(podcast_dir.glob('*.md'))
    
    if not md_files:
        print("No markdown files found")
        return
    
    modified_count = 0
    skipped_count = 0
    
    for file_path in md_files:
        if process_episode(file_path):
            modified_count += 1
        else:
            skipped_count += 1
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Modified: {modified_count} files")
    print(f"  Skipped:  {skipped_count} files")
    print(f"  Total:    {len(md_files)} files")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

