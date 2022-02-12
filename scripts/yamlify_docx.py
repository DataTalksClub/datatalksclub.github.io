#!/usr/bin/env python
# coding: utf-8

import sys
import yaml
import transcript

input_file = sys.argv[1]
output_file = sys.argv[2]


elements = transcript.read_docx(input_file)


with open(output_file, 'w') as f_out:
    yaml.dump({'transcript': elements}, f_out)


print('timecodes:')

timecodes = [
    '00:00 DataTalks.Club intro'
]


for i in range(len(elements)):
    row = elements[i]
    if 'header' not in row:
        continue
    
    if len(elements) > i:
        print('oops')
        print(row)

    next_row = elements[i + 1]
    print(row)
    print(next_row)
    print()

    time = next_row['time']

    if len(time) < 5:
        time = '0' + time

    tc = '%s %s' % (time, row['header'])
    timecodes.append(tc)

print('\n'.join(timecodes))




