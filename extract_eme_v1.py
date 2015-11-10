import re

import re
import sys
import os

#input_file = sys.argv[1]
#input_file = 'text_only_.txt'

suffixes = {'éme', 'ème', 'eme', 'émes', 'èmes', 'emes', 'iéme', 'ième', 'ieme', 'é', 'e', 'er', 'èr', 'ér', 'ere', 'ère', 'ére',
            'ÉME', 'ÈME', 'EME', 'ÉMES', 'ÈMES', 'EMES', 'IÉME', 'IÈME', 'IEME', 'É', 'E', 'ER', 'ÈR', 'ÉR', 'ERE', 'ÈRE', 'ÉRE'}
extracted_nums = set()

for file in os.listdir('files'):
    inf =  open('./files/' + file,'r', encoding='utf8')
    for line in inf:
        # print(line)
        # s = set(line.split())
        # print(s)
        # print(suffixes.intersection(s))
        # print(len(suffixes.intersection(s)))
        # if len(suffixes.intersection(s)) != 0:
        for suffix in suffixes:
            nums_in_line = re.findall('[0-9]+ ?' + suffix, line)
           # print(nums_in_line)
            extracted_nums |= set(nums_in_line)
    inf.close()
#print(sorted(extracted_nums))

outfile = open("nums.txt", 'w', encoding="utf8")
for num in sorted(extracted_nums):
    outfile.write(num + '\n')

outfile.close()

