#!/usr/bin/env python3
"""
Comprehensive script to fix all YAML quote issues in podcast files.

Handles:
1. Unclosed quotes in single-line values
2. Incorrectly split multi-line values (quote closes but content continues)
3. Unescaped double quotes inside double-quoted strings
4. Missing closing quotes in multi-line values
"""

import re
import yaml
from pathlib import Path


def fix_incorrectly_split_multiline(lines, i, field_name='intro'):
    """Fix incorrectly split multi-line values where quote closes but content continues."""
    if i >= len(lines):
        return False, 0
    
    line = lines[i]
    line_stripped = line.strip()
    
    # Check if this is an intro/description field that ends with a quote
    pattern = rf'^\s*{field_name}:\s*".*"$'
    if re.match(pattern, line_stripped):
        # Check if next line looks like it should be part of this field
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            next_stripped = next_line.strip()
            # If next line is indented and starts with text (not a key), it's probably continuation
            if next_line.startswith('  ') and not re.match(r'^\s*\w+:', next_stripped):
                # Remove closing quote from current line and merge with next
                line_fixed = line.rstrip().rstrip('"')
                next_line_fixed = next_line.lstrip()
                # Merge them
                lines[i] = line_fixed + ' ' + next_line_fixed + '\n'
                lines.pop(i + 1)
                return True, 1  # Fixed, removed 1 line
    
    return False, 0


def fix_unescaped_quotes_in_double_quoted(line):
    """Fix unescaped double quotes inside double-quoted strings."""
    # Match: field: "text with "quotes" inside"
    match = re.match(r'^(\s*(?:intro|description):\s*")(.*)(".*)$', line)
    if match:
        prefix = match.group(1)
        middle = match.group(2)
        suffix = match.group(3)
        
        # Check if middle has unescaped quotes
        if '"' in middle and '\\"' not in middle:
            # Escape all unescaped quotes in the middle
            middle_escaped = middle.replace('"', '\\"')
            return prefix + middle_escaped + suffix
    
    return line


def fix_unclosed_quotes_in_line(line, next_line=None):
    """Fix unclosed quotes in name/header/line fields."""
    patterns = [
        (r"^(\s*-?\s*(?:name|header|line):\s*)'([^']*)$", "'"),
    ]
    
    for pattern, quote_char in patterns:
        match = re.match(pattern, line)
        if match:
            prefix = match.group(1)
            value = match.group(2)
            
            if next_line:
                next_stripped = next_line.strip()
                if re.match(r'^\s*\w+:', next_stripped):
                    # Next line is a new key, current is unclosed
                    if value and not value.rstrip().endswith(quote_char):
                        value_clean = value.rstrip('\n').replace("'", "''")
                        return f"{prefix}'{value_clean}'\n"
                elif next_stripped.endswith(quote_char):
                    prefix_indent = len(prefix) - len(prefix.lstrip())
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent > prefix_indent:
                        return None  # Valid multi-line
                else:
                    prefix_indent = len(prefix) - len(prefix.lstrip())
                    next_indent = len(next_line) - len(next_line.lstrip())
                    if next_indent > prefix_indent:
                        return None  # Might be multi-line
            
            if value and not value.rstrip().endswith(quote_char):
                value_clean = value.rstrip('\n').replace("'", "''")
                return f"{prefix}'{value_clean}'\n"
    
    return None


def fix_file(file_path):
    """Fix all YAML issues in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not fm_match:
            return False, []
        
        yaml_content = fm_match.group(1)
        lines = yaml_content.splitlines(keepends=True)
        
        fixed_lines = lines.copy()
        issues_found = []
        file_modified = False
        i = 0
        
        while i < len(fixed_lines):
            line = fixed_lines[i]
            next_line = fixed_lines[i + 1] if i + 1 < len(fixed_lines) else None
            
            # Fix incorrectly split multi-line intro/description
            for field in ['intro', 'description']:
                fixed, removed = fix_incorrectly_split_multiline(fixed_lines, i, field)
                if fixed:
                    issues_found.append((i + 1, f"Incorrectly split {field} field"))
                    file_modified = True
                    # Don't increment i since we removed a line
                    continue
            
            # Fix unescaped quotes in double-quoted strings
            if 'intro:' in line or 'description:' in line:
                fixed = fix_unescaped_quotes_in_double_quoted(line)
                if fixed != line:
                    fixed_lines[i] = fixed
                    issues_found.append((i + 1, "Unescaped quotes in double-quoted string"))
                    file_modified = True
            
            # Fix unclosed quotes
            fixed = fix_unclosed_quotes_in_line(line, next_line)
            if fixed:
                fixed_lines[i] = fixed
                issues_found.append((i + 1, "Unclosed quote"))
                file_modified = True
            
            i += 1
        
        if file_modified:
            # Reconstruct full content
            fixed_yaml_content = ''.join(fixed_lines)
            # Find the frontmatter boundaries in original content
            first_dash = content.find('---\n')
            second_dash = content.find('\n---\n', first_dash + 4)
            if second_dash == -1:
                return False, issues_found
            
            # Reconstruct: before first ---, new frontmatter, after second ---
            new_content = content[:first_dash + 4] + fixed_yaml_content + content[second_dash + 1:]
            
            try:
                # Extract and test YAML
                new_fm_match = re.match(r'^---\n(.*?)\n---\n', new_content, re.DOTALL)
                if new_fm_match:
                    yaml.safe_load(new_fm_match.group(1))
                    # Write fixed file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    return True, issues_found
            except yaml.YAMLError as e:
                # Print error for debugging
                print(f"  YAML still invalid after fix: {e}")
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

