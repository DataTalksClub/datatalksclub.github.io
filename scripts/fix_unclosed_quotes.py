#!/usr/bin/env python3
"""
Script to detect and fix unclosed quotes in YAML frontmatter of markdown files.

This script scans markdown files for YAML frontmatter syntax errors caused by
unclosed quotes (single or double) and fixes them automatically.
"""

import os
import re
import sys
from pathlib import Path

import yaml
import frontmatter


def find_unclosed_quotes_in_line(line, next_line=None):
    """
    Check if a line has unclosed quotes in a YAML key-value pair.
    
    Args:
        line: The current line to check
        next_line: The next line (to check for multi-line continuation)
    
    Returns:
        tuple: (has_unclosed_quote, quote_char, fixed_line) or (False, None, None)
    """
    # Pattern to match YAML key-value pairs with quotes
    # Matches: key: 'value or key: "value (where quote isn't closed)
    patterns = [
        # Single quote pattern: key: 'value (no closing quote)
        (r"^(\s*-?\s*\w+:\s*)'([^']*)$", "'"),
        # Double quote pattern: key: "value (no closing quote)
        (r'^(\s*-?\s*\w+:\s*)"([^"]*)$', '"'),
    ]
    
    for pattern, quote_char in patterns:
        match = re.match(pattern, line)
        if match:
            prefix = match.group(1)
            value = match.group(2)
            
            # Check if this is a multi-line YAML value
            # Multi-line values continue on the next line with proper indentation
            if next_line:
                next_line_stripped = next_line.strip()
                # Check if next line starts with a key (like "startOffset:" or "url:")
                # If so, it's the next field, not a continuation - definitely unclosed
                if re.match(r'^\s*\w+:', next_line):
                    # Next line is a new key-value pair, so current line is definitely unclosed
                    # Continue to fix it below
                    pass
                # Check if next line continues the value and closes the quote
                elif next_line_stripped.endswith(quote_char):
                    # Get indentation to verify it's a continuation
                    prefix_indent = len(prefix) - len(prefix.lstrip())
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent > prefix_indent:
                        # This is a valid multi-line value, not an unclosed quote
                        return False, None, None
                # Otherwise, if next line is indented but doesn't close quote,
                # it might be a multi-line value that we can't safely fix
                else:
                    prefix_indent = len(prefix) - len(prefix.lstrip())
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent > prefix_indent:
                        # Might be multi-line, skip to avoid false positives
                        return False, None, None
            
            # Only fix if the value doesn't end with a quote and isn't empty
            if value and not value.rstrip().endswith(quote_char):
                # Remove trailing newline from value if present, we'll add it back
                value_clean = value.rstrip('\n')
                fixed_line = f"{prefix}{quote_char}{value_clean}{quote_char}\n"
                return True, quote_char, fixed_line
    
    return False, None, None


def fix_unclosed_quotes_in_file(file_path):
    """
    Fix unclosed quotes in a markdown file's YAML frontmatter.
    
    Returns:
        tuple: (fixed, issues_found) where fixed is bool and issues_found is list of (line_num, description)
    """
    issues_found = []
    
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not fm_match:
            # No frontmatter found, skip
            return False, []
        
        yaml_content = fm_match.group(1)
        
        # Split content into lines for processing
        lines = content.splitlines(keepends=True)
        
        # Find YAML frontmatter boundaries
        frontmatter_start = None
        frontmatter_end = None
        
        for i, line in enumerate(lines):
            if line.strip() == '---':
                if frontmatter_start is None:
                    frontmatter_start = i
                else:
                    frontmatter_end = i
                    break
        
        if frontmatter_start is None or frontmatter_end is None:
            return False, []
        
        # Always check for unclosed quotes in frontmatter, even if YAML parses
        # (YAML parsers can be lenient and accept invalid syntax)
        fixed_lines = lines.copy()
        file_modified = False
        
        for i in range(frontmatter_start + 1, frontmatter_end):
            if i >= len(lines):
                break
            line = lines[i]
            # Get next line if available
            next_line = lines[i + 1] if i + 1 < len(lines) else None
            has_issue, quote_char, fixed_line = find_unclosed_quotes_in_line(line, next_line)
            
            if has_issue:
                line_num = i + 1  # 1-indexed for reporting
                issues_found.append((line_num, f"Unclosed {quote_char} quote"))
                fixed_lines[i] = fixed_line
                file_modified = True
            
            # If we found issues, try to fix and verify
            if file_modified:
                fixed_content = ''.join(fixed_lines)
                try:
                    # Extract frontmatter and try to parse it
                    fm_match = re.match(r'^---\n(.*?)\n---\n', fixed_content, re.DOTALL)
                    if fm_match:
                        yaml_content = fm_match.group(1)
                        yaml.safe_load(yaml_content)  # Try to parse
                        
                        # If parsing succeeds, write the file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(fixed_content)
                        
                        return True, issues_found
                    else:
                        print(f"Warning: Could not extract frontmatter from {file_path}")
                        return False, issues_found
                except yaml.YAMLError as e2:
                    # Still has errors, but we tried
                    return False, issues_found
            
            return False, issues_found
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []


def main():
    """Main function to scan and fix all podcast markdown files."""
    # Get the script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    podcast_dir = project_root / '_podcast'
    
    if not podcast_dir.exists():
        print(f"Error: Podcast directory not found: {podcast_dir}")
        sys.exit(1)
    
    # Find all markdown files
    md_files = list(podcast_dir.glob('*.md'))
    
    print(f"Scanning {len(md_files)} markdown files for unclosed quotes...\n")
    
    total_fixed = 0
    total_issues = 0
    
    for md_file in sorted(md_files):
        fixed, issues = fix_unclosed_quotes_in_file(md_file)
        
        if issues:
            total_issues += len(issues)
            if fixed:
                total_fixed += 1
                print(f"✓ Fixed {md_file.name}:")
                for line_num, description in issues:
                    print(f"    Line {line_num}: {description}")
            else:
                print(f"⚠ Found issues in {md_file.name} (could not auto-fix):")
                for line_num, description in issues:
                    print(f"    Line {line_num}: {description}")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files scanned: {len(md_files)}")
    print(f"  Files fixed: {total_fixed}")
    print(f"  Total issues found: {total_issues}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

