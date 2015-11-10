'''
Запускать так:
название_скрипта файл_со_списком
'''


import sys
import re

input_file = sys.argv[1]
#input_file = "qwe.txt"

inf = open(input_file, 'r', encoding="utf8")
ouf2 = open(re.sub("\.txt", "", input_file) + "_no_doublicates.txt", 'w', encoding="utf8")
ouf = open(re.sub("\.txt", "", input_file) + "_doublicates.txt", 'w', encoding="utf8")


list_of_words = []

for line in inf:
    if line not in list_of_words:
        list_of_words.append(line)
        ouf2.write(line)
    else:
        ouf.write(line)


print('So Long, and Thanks for all the Fish!')

inf.close()
ouf.close()
ouf2.close()

