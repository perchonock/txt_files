'''
Запускать так:
название_скрипта файл_со_списком
'''


import sys
import re

#input_file = sys.argv[1]
input_file = "urls404.txt"

inf = open(input_file, 'r', encoding="utf8")
ouf2 = open(re.sub("\.txt", "", input_file) + "_no_doublicates.txt", 'w', encoding="utf8")
ouf = open(re.sub("\.txt", "", input_file) + "_doublicates.txt", 'w', encoding="utf8")


items = set()

for line in inf:
    line = line.strip('\n').strip()
    if line not in items:
        items.add(line)
        ouf2.write(line + '\n')
    else:
        ouf.write(line + '\n')


print('So Long, and Thanks for all the Fish!')

inf.close()
ouf.close()
ouf2.close()
