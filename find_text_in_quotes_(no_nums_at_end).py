'''
Запускать так:
название_скрипта файл_с_текстом
'''

import re
import sys

input_file = sys.argv[1]
#input_file = 'test4find_quotes.txt'

infile = open(input_file,'r', encoding='utf8')
outfile = open(re.sub("\.txt", "", input_file) + "_quotes.txt", 'w', encoding="utf8")

all_quotes = set()
for line in infile:
    quotes = re.findall(r'"[^"]*"', line)
    if quotes != []:
        for i in quotes:
            m = re.search('\d+"$', i)
            if m is None:
                all_quotes.add(i)

for i in all_quotes:
    outfile.write(i + "\n")

#quotes = re.findall('"[^"^\u201d]*["\u201d]', buffer)
infile.close()
outfile.close()


