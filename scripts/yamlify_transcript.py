#!/usr/bin/env python

import json
import yaml
import re

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


def clean_line(line):
    line = line.strip()
    line = line.strip('\uFEFF')
    return line

with open(input_file) as f_in:
    lines = []
    for line in f_in:
        line = clean_line(line)
        if line:
            lines.append(line)


ts_two_digit_pattern = re.compile(r'^(\d+):(\d+)$')
ts_three_digit_pattern = re.compile(r'^\[?(\d+):(\d+):(\d+)\]?$')


def format_time(h, m, s):
    if h > 0:
        return '%d:%02d:%02d' % (h, m, s)
    return '%d:%02d' % (m, s)


def try_parse_time(line):
    match = ts_two_digit_pattern.match(line)

    if match is not None:
        m, s = int(match.group(1)), int(match.group(2))
        h = m // 60
        m = m % 60
        return h, m, s

    match = ts_three_digit_pattern.match(line)
    if match is not None:
        h = int(match.group(1))
        m = int(match.group(2))
        s = int(match.group(3))
        return h, m, s

    return None


def parse_lines(lines):
    i = 0
    n = len(lines)

    results = []

    while i < n:
        raw_line = lines[i]

        match = try_parse_time(raw_line)

        if match is None:
            row = {
               'header': raw_line 
            }
            results.append(row)
            i = i + 1
        else:
            h, m, s = match
            total_sec = h * 60 * 60 + m * 60 + s

            who = lines[i + 1].strip().rstrip(':')
            line = lines[i + 2]

            row = {
                'time': format_time(h, m, s),
                'sec': total_sec,
                'who': who,
                'line': line
            }
            results.append(row)

            i = i + 3

            while (i < n) and lines[i].startswith('='):
                line = lines[i].lstrip('=').strip()
                row = {
                    'who': who,
                    'line': line
                }
                results.append(row)
                i = i + 1

    return results


results = parse_lines(lines)


with open(output_file, 'w') as f_out:
    yaml.dump({'transcript': results}, f_out)


print('timecodes:')

timecodes = [
    '00:00 DataTalks.Club intro'
]


for i in range(len(results)):
    row = results[i]
    if 'header' not in row:
        continue

    next_row = results[i + 1]
    time = next_row['time']

    if len(time) < 5:
        time = '0' + time

    tc = '%s %s' % (time, row['header'])
    timecodes.append(tc)

print('\n'.join(timecodes))