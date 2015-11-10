'''
Запускать так:
название_скрипта файл_с_текстом
'''

import re
import sys

input_file = sys.argv[1]
#input_file = 'text_only_.txt'

infile = open(input_file,'r', encoding='utf8')
outfile = open(re.sub("\.txt", "", input_file) + "_quotes.txt", 'w', encoding="utf8")

all_quotes = set()
for line in infile:
    quotes = re.findall(r'"[^"]*"', line)
    if quotes != []:
        for i in quotes:
            all_quotes.add(i)

for i in all_quotes:
    outfile.write(i + "\n")

#quotes = re.findall('"[^"^\u201d]*["\u201d]', buffer)
infile.close()
outfile.close()


