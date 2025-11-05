#!/usr/bin/env python3
"""
Batch generate meta descriptions for multiple podcast episodes.

Usage:
    python batch_generate_meta_descriptions.py [--pattern PATTERN] [--update] [--skip-existing]
    
Example:
    # Process all podcasts in to-update-top-10 folder
    python batch_generate_meta_descriptions.py --pattern "_podcast/to-update-top-10/*.md" --update
    
    # Process all season 22 episodes
    python batch_generate_meta_descriptions.py --pattern "_podcast/s22*.md" --update
    
    # Process all podcasts but skip those that already have descriptions
    python batch_generate_meta_descriptions.py --pattern "_podcast/*.md" --update --skip-existing
"""

import argparse
import glob
import sys
import time
from pathlib import Path
from generate_meta_descriptions import (
    parse_podcast_file,
    generate_meta_description,
    update_podcast_file
)


def process_file(file_path, update=False, skip_existing=False, api_key=None):
    """Process a single file and return results."""
    try:
        # Read file content
        file_content = parse_podcast_file(file_path)
        
        # Check if description exists and skip if requested (simple check in content)
        if skip_existing and 'description:' in file_content:
            return {
                'status': 'skipped',
                'file': file_path.name,
                'reason': 'already has description'
            }
        
        # Generate description
        meta_description = generate_meta_description(file_content, api_key=api_key)
        
        # Update file if requested
        if update:
            success = update_podcast_file(file_path, meta_description)
            if not success:
                return {
                    'status': 'error',
                    'file': file_path.name,
                    'error': 'Failed to update file'
                }
        
        return {
            'status': 'success',
            'file': file_path.name,
            'description': meta_description,
            'length': len(meta_description),
            'updated': update,
            'had_existing': bool(existing_description)
        }
    
    except Exception as e:
        return {
            'status': 'error',
            'file': file_path.name,
            'error': str(e)
        }


def main():
    parser = argparse.ArgumentParser(
        description='Batch generate meta descriptions for podcast episodes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process all podcasts in to-update-top-10 folder (preview only)
  python batch_generate_meta_descriptions.py --pattern "_podcast/to-update-top-10/*.md"
  
  # Process and update all season 22 episodes
  python batch_generate_meta_descriptions.py --pattern "_podcast/s22*.md" --update
  
  # Process all podcasts, skip those with existing descriptions
  python batch_generate_meta_descriptions.py --pattern "_podcast/*.md" --update --skip-existing
  
  # Process specific files
  python batch_generate_meta_descriptions.py --files s22e01.md s22e02.md --update
        """
    )
    
    parser.add_argument('--pattern', default='_podcast/*.md',
                       help='Glob pattern for files to process (default: _podcast/*.md)')
    parser.add_argument('--files', nargs='+',
                       help='Specific files to process')
    parser.add_argument('--update', action='store_true',
                       help='Update files with generated descriptions')
    parser.add_argument('--skip-existing', action='store_true',
                       help='Skip files that already have a description')
    parser.add_argument('--api-key', help='OpenAI API key (or set OPENAI_API_KEY env var)')
    parser.add_argument('--delay', type=float, default=1.0,
                       help='Delay between API calls in seconds (default: 1.0)')
    parser.add_argument('--limit', type=int,
                       help='Maximum number of files to process')
    
    args = parser.parse_args()
    
    # Get list of files to process
    if args.files:
        file_paths = [Path(f) for f in args.files]
    else:
        file_paths = [Path(f) for f in glob.glob(args.pattern, recursive=True)]
    
    # Filter out non-markdown files and non-existent files
    file_paths = [f for f in file_paths if f.exists() and f.suffix == '.md']
    
    # Sort files
    file_paths.sort()
    
    # Apply limit if specified
    if args.limit:
        file_paths = file_paths[:args.limit]
    
    if not file_paths:
        print("No files found matching the pattern.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(file_paths)} file(s) to process")
    print(f"Mode: {'UPDATE' if args.update else 'PREVIEW ONLY'}")
    print(f"Skip existing: {'YES' if args.skip_existing else 'NO'}")
    print("=" * 60)
    print()
    
    # Process files
    results = []
    for i, file_path in enumerate(file_paths, 1):
        print(f"[{i}/{len(file_paths)}] Processing: {file_path.name}")
        
        result = process_file(
            file_path,
            update=args.update,
            skip_existing=args.skip_existing,
            api_key=args.api_key
        )
        
        results.append(result)
        
        # Display result
        if result['status'] == 'success':
            desc = result['description']
            length = result['length']
            
            # Truncate for display
            display_desc = desc if len(desc) <= 80 else desc[:77] + "..."
            
            status_icon = '✓'
            length_warning = ''
            if length > 160:
                length_warning = f' ⚠️  (too long: {length} chars)'
            elif length < 140:
                length_warning = f' ℹ️  (short: {length} chars)'
            
            print(f"  {status_icon} {display_desc}")
            print(f"    Length: {length} chars{length_warning}")
            
            if result['had_existing']:
                print(f"    (Replaced existing description)")
            
            if args.update:
                print(f"    ✓ File updated")
        
        elif result['status'] == 'skipped':
            print(f"  ⊘ Skipped: {result['reason']}")
        
        elif result['status'] == 'error':
            print(f"  ✗ Error: {result['error']}", file=sys.stderr)
        
        print()
        
        # Delay between requests to avoid rate limits
        if i < len(file_paths):
            time.sleep(args.delay)
    
    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("-" * 60)
    
    success_count = sum(1 for r in results if r['status'] == 'success')
    skipped_count = sum(1 for r in results if r['status'] == 'skipped')
    error_count = sum(1 for r in results if r['status'] == 'error')
    
    print(f"Total files: {len(results)}")
    print(f"Successful: {success_count}")
    print(f"Skipped: {skipped_count}")
    print(f"Errors: {error_count}")
    
    if success_count > 0:
        lengths = [r['length'] for r in results if r['status'] == 'success']
        avg_length = sum(lengths) / len(lengths)
        too_long = sum(1 for l in lengths if l > 160)
        too_short = sum(1 for l in lengths if l < 140)
        optimal = sum(1 for l in lengths if 140 <= l <= 155)
        
        print()
        print("Description lengths:")
        print(f"  Average: {avg_length:.1f} chars")
        print(f"  Optimal (140-155): {optimal}")
        print(f"  Too short (<140): {too_short}")
        print(f"  Too long (>160): {too_long}")
    
    if error_count > 0:
        print("\nErrors occurred:")
        for r in results:
            if r['status'] == 'error':
                print(f"  - {r['file']}: {r['error']}")
    
    if not args.update and success_count > 0:
        print("\n💡 Run with --update flag to save changes to files")


if __name__ == '__main__':
    main()

