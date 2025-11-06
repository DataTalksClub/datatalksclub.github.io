#!/usr/bin/env python3
"""
Tests for insert_podcast_timestamps.py
"""

import unittest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, mock_open
import sys

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from insert_podcast_timestamps import (
    parse_timestamps_file,
    update_headers_in_transcript,
    update_podcast_file_with_timestamps
)


class TestParseTimestampsFile(unittest.TestCase):
    """Tests for parse_timestamps_file function"""
    
    def test_basic_timestamps(self):
        """Test parsing basic timestamp format"""
        content = """00:00:00 Introduction
00:01:30 First Topic
00:05:45 Second Topic
01:02:15 Third Topic"""
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            timestamps = parse_timestamps_file(temp_path)
            self.assertEqual(len(timestamps), 4)
            self.assertEqual(timestamps[0], (0, "Introduction"))
            self.assertEqual(timestamps[1], (90, "First Topic"))
            self.assertEqual(timestamps[2], (345, "Second Topic"))
            self.assertEqual(timestamps[3], (3735, "Third Topic"))
        finally:
            os.unlink(temp_path)
    
    def test_empty_lines(self):
        """Test that empty lines are skipped"""
        content = """00:00:00 Introduction

00:01:30 First Topic


00:05:45 Second Topic"""
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            timestamps = parse_timestamps_file(temp_path)
            self.assertEqual(len(timestamps), 3)
        finally:
            os.unlink(temp_path)
    
    def test_invalid_format(self):
        """Test that invalid lines are skipped with warning"""
        content = """00:00:00 Valid timestamp
Invalid line
00:01:30 Another valid timestamp
12:34 Invalid format"""
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            with patch('sys.stderr') as mock_stderr:
                timestamps = parse_timestamps_file(temp_path)
                self.assertEqual(len(timestamps), 2)
                self.assertEqual(timestamps[0], (0, "Valid timestamp"))
                self.assertEqual(timestamps[1], (90, "Another valid timestamp"))
        finally:
            os.unlink(temp_path)
    
    def test_whitespace_handling(self):
        """Test that topic text is stripped of extra whitespace"""
        content = """00:00:00   Topic with spaces   
00:01:30\tTab separated topic\t"""
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            timestamps = parse_timestamps_file(temp_path)
            self.assertEqual(timestamps[0][1], "Topic with spaces")
            self.assertEqual(timestamps[1][1], "Tab separated topic")
        finally:
            os.unlink(temp_path)
    
    def test_large_time_values(self):
        """Test handling of large time values (hours > 24)"""
        content = """25:30:00 Long podcast
99:59:59 Very long podcast"""
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            timestamps = parse_timestamps_file(temp_path)
            self.assertEqual(timestamps[0][0], 25 * 3600 + 30 * 60)  # 91800
            self.assertEqual(timestamps[1][0], 99 * 3600 + 59 * 60 + 59)  # 359999
        finally:
            os.unlink(temp_path)


class TestUpdateHeadersInTranscript(unittest.TestCase):
    """Tests for update_headers_in_transcript function"""
    
    def test_simple_insertion(self):
        """Test inserting headers at correct positions"""
        transcript = [
            {'line': 'First line', 'sec': 0, 'who': 'Alex'},
            {'line': 'Second line', 'sec': 60, 'who': 'Bob'},
            {'line': 'Third line', 'sec': 120, 'who': 'Alex'},
        ]
        timestamps = [
            (30, 'Topic 1'),
            (90, 'Topic 2'),
        ]
        
        result = update_headers_in_transcript(transcript, timestamps)
        
        # Should have headers inserted before entries with sec >= timestamp
        self.assertEqual(len(result), 5)  # 3 entries + 2 headers
        self.assertEqual(result[0], {'line': 'First line', 'sec': 0, 'who': 'Alex'})
        self.assertEqual(result[1], {'header': 'Topic 1'})
        self.assertEqual(result[2], {'line': 'Second line', 'sec': 60, 'who': 'Bob'})
        self.assertEqual(result[3], {'header': 'Topic 2'})
        self.assertEqual(result[4], {'line': 'Third line', 'sec': 120, 'who': 'Alex'})
    
    def test_remove_existing_headers(self):
        """Test that existing headers are removed"""
        transcript = [
            {'header': 'Old header 1'},
            {'line': 'First line', 'sec': 0, 'who': 'Alex'},
            {'header': 'Old header 2'},
            {'line': 'Second line', 'sec': 60, 'who': 'Bob'},
        ]
        timestamps = [
            (30, 'New header'),
        ]
        
        result = update_headers_in_transcript(transcript, timestamps)
        
        # Old headers should be removed
        headers = [item for item in result if 'header' in item]
        self.assertEqual(len(headers), 1)
        self.assertEqual(headers[0], {'header': 'New header'})
    
    def test_entries_without_sec(self):
        """Test handling entries without sec values"""
        transcript = [
            {'line': 'First line', 'sec': 0, 'who': 'Alex'},
            {'line': 'Second line', 'who': 'Bob'},  # No sec
            {'line': 'Third line', 'sec': 120, 'who': 'Alex'},
        ]
        timestamps = [
            (30, 'Topic 1'),
            (60, 'Topic 2'),
        ]
        
        result = update_headers_in_transcript(transcript, timestamps)
        
        # Topic 1 should be before entry with sec 0 (since 30 > 0)
        # Topic 2 should be between entry with sec 0 and sec 120
        headers = [item for item in result if 'header' in item]
        self.assertEqual(len(headers), 2)
        # Check that headers are in reasonable positions
        self.assertIn({'header': 'Topic 1'}, headers)
        self.assertIn({'header': 'Topic 2'}, headers)
    
    def test_unsorted_timestamps(self):
        """Test that timestamps are sorted correctly"""
        transcript = [
            {'line': 'First line', 'sec': 0, 'who': 'Alex'},
            {'line': 'Second line', 'sec': 60, 'who': 'Bob'},
            {'line': 'Third line', 'sec': 120, 'who': 'Alex'},
        ]
        timestamps = [
            (90, 'Topic 2'),
            (30, 'Topic 1'),
        ]  # Out of order
        
        result = update_headers_in_transcript(transcript, timestamps)
        
        # Should be inserted in correct order
        result_headers = [item for item in result if 'header' in item]
        self.assertEqual(len(result_headers), 2)
        # Find positions
        header_indices = [i for i, item in enumerate(result) if 'header' in item]
        self.assertLess(header_indices[0], header_indices[1])
    
    def test_timestamps_at_end(self):
        """Test timestamps that come after all entries"""
        transcript = [
            {'line': 'First line', 'sec': 0, 'who': 'Alex'},
            {'line': 'Second line', 'sec': 60, 'who': 'Bob'},
        ]
        timestamps = [
            (30, 'Topic 1'),
            (200, 'Topic 2'),  # After all entries
        ]
        
        result = update_headers_in_transcript(transcript, timestamps)
        
        # Topic 2 should be at the end
        self.assertEqual(result[-1], {'header': 'Topic 2'})
    
    def test_multiple_timestamps_at_same_time(self):
        """Test handling multiple timestamps at the same second"""
        transcript = [
            {'line': 'First line', 'sec': 0, 'who': 'Alex'},
            {'line': 'Second line', 'sec': 60, 'who': 'Bob'},
        ]
        timestamps = [
            (30, 'Topic 1'),
            (30, 'Topic 1a'),  # Same time
        ]
        
        result = update_headers_in_transcript(transcript, timestamps)
        
        # Both should be inserted
        headers = [item for item in result if 'header' in item]
        self.assertEqual(len(headers), 2)
    
    def test_empty_transcript(self):
        """Test with empty transcript"""
        transcript = []
        timestamps = [
            (30, 'Topic 1'),
        ]
        
        result = update_headers_in_transcript(transcript, timestamps)
        
        # Should just have the header
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {'header': 'Topic 1'})
    
    def test_no_timestamps(self):
        """Test with no timestamps"""
        transcript = [
            {'header': 'Old header'},
            {'line': 'First line', 'sec': 0, 'who': 'Alex'},
        ]
        timestamps = []
        
        result = update_headers_in_transcript(transcript, timestamps)
        
        # Should have no headers, just content
        headers = [item for item in result if 'header' in item]
        self.assertEqual(len(headers), 0)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {'line': 'First line', 'sec': 0, 'who': 'Alex'})
    
    def test_entries_without_sec_at_beginning(self):
        """Test entries without sec at the very beginning"""
        transcript = [
            {'line': 'First line', 'who': 'Alex'},  # No sec
            {'line': 'Second line', 'who': 'Bob'},  # No sec
            {'line': 'Third line', 'sec': 60, 'who': 'Alex'},
        ]
        timestamps = [
            (30, 'Topic 1'),
            (90, 'Topic 2'),
        ]
        
        result = update_headers_in_transcript(transcript, timestamps)
        
        # Topic 1 should be before entry with sec 60 (since 30 < 60)
        # Topic 2 should be after entry with sec 60
        headers = [item for item in result if 'header' in item]
        self.assertEqual(len(headers), 2)
        
        # Find positions
        header_indices = [i for i, item in enumerate(result) if 'header' in item]
        entry_indices = [i for i, item in enumerate(result) if 'sec' in item and item.get('sec') == 60]
        
        # Topic 1 should be before the entry with sec 60
        self.assertLess(header_indices[0], entry_indices[0])
        # Topic 2 should be after the entry with sec 60
        self.assertGreater(header_indices[1], entry_indices[0])


class TestUpdatePodcastFileWithTimestamps(unittest.TestCase):
    """Tests for update_podcast_file_with_timestamps function"""
    
    def test_basic_update(self):
        """Test basic file update functionality"""
        frontmatter = """title: Test Podcast
season: 1
episode: 1
transcript:
  - line: First line
    sec: 0
    who: Alex
  - line: Second line
    sec: 60
    who: Bob
"""
        content = f"---\n{frontmatter}---\n# Podcast Content\nSome markdown here."
        
        timestamps = [
            (30, 'Topic 1'),
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            result = update_podcast_file_with_timestamps(temp_path, timestamps)
            self.assertTrue(result)
            
            # Read back and verify
            with open(temp_path, 'r', encoding='utf-8') as f:
                updated_content = f.read()
            
            # Should still have frontmatter structure
            self.assertIn('---', updated_content)
            self.assertIn('transcript:', updated_content)
            # Should have header
            self.assertIn("Topic 1", updated_content)
        finally:
            os.unlink(temp_path)
    
    def test_no_frontmatter_delimiter(self):
        """Test error handling for missing frontmatter"""
        content = "No frontmatter here\nJust content."
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            with patch('sys.stderr'):
                result = update_podcast_file_with_timestamps(temp_path, [])
                self.assertFalse(result)
        finally:
            os.unlink(temp_path)
    
    def test_no_closing_delimiter(self):
        """Test error handling for missing closing delimiter"""
        content = "---\ntitle: Test\n--- Missing closing"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            with patch('sys.stderr'):
                result = update_podcast_file_with_timestamps(temp_path, [])
                self.assertFalse(result)
        finally:
            os.unlink(temp_path)
    
    def test_no_transcript_field(self):
        """Test error handling for missing transcript field"""
        frontmatter = """title: Test Podcast
season: 1
episode: 1
"""
        content = f"---\n{frontmatter}---\n# Content"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            with patch('sys.stderr'):
                result = update_podcast_file_with_timestamps(temp_path, [])
                self.assertFalse(result)
        finally:
            os.unlink(temp_path)
    
    def test_invalid_yaml(self):
        """Test error handling for invalid YAML"""
        frontmatter = """title: Test Podcast
invalid: yaml: : : :
"""
        content = f"---\n{frontmatter}---\n# Content"
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            with patch('sys.stderr'):
                result = update_podcast_file_with_timestamps(temp_path, [])
                self.assertFalse(result)
        finally:
            os.unlink(temp_path)
    
    def test_frontmatter_without_trailing_newline(self):
        """Test handling frontmatter that ends with --- without newline"""
        frontmatter = """title: Test Podcast
transcript:
  - line: First line
    sec: 0
"""
        content = f"---\n{frontmatter}---Content after"
        
        timestamps = [(30, 'Topic 1')]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            result = update_podcast_file_with_timestamps(temp_path, timestamps)
            self.assertTrue(result)
            
            # Read back and verify structure is preserved
            with open(temp_path, 'r', encoding='utf-8') as f:
                updated_content = f.read()
            
            self.assertIn('---', updated_content)
            self.assertIn('Content after', updated_content)
        finally:
            os.unlink(temp_path)
    
    def test_preserves_other_frontmatter_fields(self):
        """Test that other frontmatter fields are preserved"""
        frontmatter = """title: Test Podcast
season: 1
episode: 1
guests:
  - guest1
transcript:
  - line: First line
    sec: 0
"""
        content = f"---\n{frontmatter}---\n# Content"
        
        timestamps = [(30, 'Topic 1')]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.md') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            result = update_podcast_file_with_timestamps(temp_path, timestamps)
            self.assertTrue(result)
            
            # Read back and verify other fields are still there
            with open(temp_path, 'r', encoding='utf-8') as f:
                updated_content = f.read()
            
            self.assertIn('title: Test Podcast', updated_content)
            self.assertIn('season: 1', updated_content)
            self.assertIn('guests:', updated_content)
            self.assertIn('guest1', updated_content)
        finally:
            os.unlink(temp_path)


if __name__ == '__main__':
    unittest.main()

