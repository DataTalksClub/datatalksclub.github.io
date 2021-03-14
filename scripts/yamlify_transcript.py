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


ts = re.compile(r'^(\d+):(\d+)$')


def convert_time(m, s):
    h = m // 60
    if h > 0:
        return '%d:%02d:%02d' % (h, m % 60, s)
    return '%d:%02d' % (m, s)


def parse_lines(lines):
    i = 0
    n = len(lines)

    results = []

    while i < n:
        raw_line = lines[i]

        match = ts.match(raw_line)

        if match is None:
            row = {
               'header': raw_line 
            }
            i = i + 1
        else:
            m, s = int(match.group(1)), int(match.group(2))
            total_sec = m * 60 + s

            who = lines[i + 1]
            line = lines[i + 2]

            row = {
                'time': convert_time(m, s),
                'sec': total_sec,
                'who': who,
                'line': line
            }

            i = i + 3

        results.append(row)

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
    time = results[i + 1]['time']
    if len(time) < 5:
        time = '0' + time
    tc = '%s %s' % (time, row['header'])
    timecodes.append(tc)

print('\n'.join(timecodes))