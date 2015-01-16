'''
Запускать так:
название_скрипта файл_с_текстом файл_со_списком_фраз
'''

import sys
import re

text_file = sys.argv[1]
list_of_phrases = sys.argv[2]

inf = open(text_file, 'r', encoding="utf8")
ngrams = open(list_of_phrases, 'r', encoding="utf8")
ouf = open(re.sub("\.txt", "", list_of_phrases) + "_with_freq.txt", 'w', encoding="utf8")

phrases_dict = {}

for line in ngrams:
    phrases_dict[line.strip()] = 0

#print(phrases_dict)

for line in inf:
    for phrase in phrases_dict:
        if phrase.lower() in line.strip().lower():
            phrases_dict[phrase] +=1

for key, value in phrases_dict.items():
    s = key + "\t" + str(value) + "\n"
    ouf.write(s)

#print(phrases_dict)

inf.close()
ngrams.close()
ouf.close()
