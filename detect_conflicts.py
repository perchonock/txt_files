'''
Запускать так:
название_скрипта файл_со_списком
'''


import sys
import re

# input_file = sys.argv[1]
input_file = "test4detect_conflicts.txt"

inf = open(input_file, 'r', encoding="utf8")
ouf = open(re.sub("\.txt", "", input_file) + "_conflicts.txt", 'w', encoding="utf8")

list_of_words = []

for line in inf:
    list_of_words.append(line.strip().split('\t'))

list_of_words.sort()
print(list_of_words)

ln = len(list_of_words)
for i in range(ln-1):
    if list_of_words[i][0] == list_of_words[i+1][0] and list_of_words[i][1] != list_of_words[i+1][1]:
        s = list_of_words[i][0] + '\t' + list_of_words[i][1] + '\n' + list_of_words[i+1][0] + '\t' + list_of_words[i+1][1] + '\n'
        ouf.write(s)

print('So Long, and Thanks for all the Fish!')

inf.close()
ouf.close()

