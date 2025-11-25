#!/usr/bin/env python3
"""
Comprehensive script to fix all YAML quote issues in podcast files.
Handles:
1. Unclosed quotes in quotableClips and transcript sections
2. Double quotes inside double-quoted strings (need escaping)
3. Apostrophes in single-quoted strings (need doubling)
"""

import re
import yaml
from pathlib import Path


def fix_double_quotes_in_double_quoted_string(line):
    """Fix double quotes inside double-quoted strings by escaping them."""
    # Pattern: field: "text with "quotes" inside"
    # Need to escape internal quotes: field: "text with \"quotes\" inside"
    
    # Match lines like: intro: "text with "quotes" inside"
    pattern = r'^(\s*\w+:\s*)"([^"]*)"([^"]*)"([^"]*)"'
    
    def escape_quotes(match):
        prefix = match.group(1)
        part1 = match.group(2)
        quoted_part = match.group(3)
        part2 = match.group(4)
        
        # Check if this is actually a double-quoted string that continues
        # If part2 ends with quote, it's the closing quote
        if part2.endswith('"'):
            # This is: field: "text "quoted" text"
            # Should be: field: "text \"quoted\" text"
            return f'{prefix}"{part1}\\"{quoted_part}\\"{part2}'
        return match.group(0)
    
    # More comprehensive: find all "text" patterns inside a double-quoted field
    # Match: field: "start "middle" end"
    new_line = line
    if ':' in line and line.count('"') >= 4:  # At least 2 pairs of quotes
        # Check if it starts with a field and double quote
        field_match = re.match(r'^(\s*\w+:\s*)"', line)
        if field_match:
            # This is a field with double quotes
            # Find unescaped quotes after the opening quote
            prefix = field_match.group(1)
            rest = line[len(prefix) + 1:]  # After the opening quote
            
            # If the line doesn't end with a quote, it might be multi-line
            if not rest.rstrip().endswith('"'):
                return line  # Multi-line, skip for now
            
            # Count quotes - if odd, there's a problem
            quote_count = rest.count('"')
            if quote_count % 2 == 1:  # Should be even (pairs)
                # Try to escape internal quotes
                # Simple approach: escape all quotes except the last one
                parts = rest.rsplit('"', 1)
                if len(parts) == 2:
                    content = parts[0]
                    suffix = parts[1] + '"'
                    # Escape all quotes in content
                    content_escaped = content.replace('"', '\\"')
                    new_line = f'{prefix}"{content_escaped}{suffix}'
    
    return new_line


def fix_unclosed_quotes_in_line(line, next_line=None):
    """Fix unclosed quotes in a line."""
    # Check for unclosed single quotes in name/header/line fields
    patterns = [
        (r"^(\s*-?\s*(?:name|header|line):\s*)'([^']*)$", "'"),
    ]
    
    for pattern, quote_char in patterns:
        match = re.match(pattern, line)
        if match:
            prefix = match.group(1)
            value = match.group(2)
            
            # Check if next line is a continuation or new field
            if next_line:
                next_stripped = next_line.strip()
                # If next line starts with a key, current is unclosed
                if re.match(r'^\s*\w+:', next_stripped):
                    if value and not value.rstrip().endswith(quote_char):
                        # Remove trailing newline if present
                        value_clean = value.rstrip('\n')
                        # Handle apostrophes - double them for YAML
                        value_clean = value_clean.replace("'", "''")
                        return f"{prefix}'{value_clean}'\n"
                # If next line is indented and ends with quote, it's multi-line (valid)
                elif next_stripped.endswith(quote_char):
                    prefix_indent = len(prefix) - len(prefix.lstrip())
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent > prefix_indent:
                        return None  # Valid multi-line
            
            # Single line unclosed
            if value and not value.rstrip().endswith(quote_char):
                value_clean = value.rstrip('\n')
                value_clean = value_clean.replace("'", "''")  # Escape apostrophes
                return f"{prefix}'{value_clean}'\n"
    
    return None


def fix_file(file_path):
    """Fix all YAML quote issues in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not fm_match:
            return False, []
        
        lines = content.splitlines(keepends=True)
        
        # Find frontmatter boundaries
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
        
        fixed_lines = lines.copy()
        issues_found = []
        file_modified = False
        
        # Fix issues in frontmatter
        for i in range(frontmatter_start + 1, frontmatter_end):
            if i >= len(lines):
                break
            
            line = lines[i]
            next_line = lines[i + 1] if i + 1 < len(lines) else None
            
            # Fix unclosed quotes
            fixed = fix_unclosed_quotes_in_line(line, next_line)
            if fixed:
                fixed_lines[i] = fixed
                issues_found.append((i + 1, "Unclosed quote"))
                file_modified = True
                continue
            
            # Fix double quotes in double-quoted strings (intro, description fields)
            if 'intro:' in line or 'description:' in line:
                fixed = fix_double_quotes_in_double_quoted_string(line)
                if fixed != line:
                    fixed_lines[i] = fixed
                    issues_found.append((i + 1, "Unescaped quotes in double-quoted string"))
                    file_modified = True
        
        if file_modified:
            # Verify fix
            fixed_content = ''.join(fixed_lines)
            fm_match = re.match(r'^---\n(.*?)\n---\n', fixed_content, re.DOTALL)
            if fm_match:
                try:
                    yaml.safe_load(fm_match.group(1))
                    # Write fixed file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(fixed_content)
                    return True, issues_found
                except yaml.YAMLError:
                    return False, issues_found
        
        return False, issues_found
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, []


def main():
    """Main function."""
    podcast_dir = Path('_podcast')
    md_files = list(podcast_dir.glob('*.md'))
    
    print(f"Scanning {len(md_files)} files for YAML quote issues...\n")
    
    total_fixed = 0
    total_issues = 0
    
    for md_file in sorted(md_files):
        fixed, issues = fix_file(md_file)
        if issues:
            total_issues += len(issues)
            if fixed:
                total_fixed += 1
                print(f"✓ Fixed {md_file.name}: {len(issues)} issue(s)")
            else:
                print(f"⚠ {md_file.name}: Found {len(issues)} issue(s) but couldn't auto-fix")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files scanned: {len(md_files)}")
    print(f"  Files fixed: {total_fixed}")
    print(f"  Total issues found: {total_issues}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

