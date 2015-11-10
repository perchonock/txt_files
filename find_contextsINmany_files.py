__author__ = 'YKolotolova'

import sys
import re
import os

list_of_words = sys.argv[1]
# in_file = 'text_only.txt.001'
# list_of_words = "ina_unknown.txt"
ouf = open("contexts.txt", 'w', encoding='utf16')
words_file = open(list_of_words, "r", encoding='utf8')

searched_words = set()
for line in words_file:
    searched_words.add(line.strip().lower())

#print("searched words", searched_words)

for file in os.listdir('files'):
    inf =  open('./files/' + file,'r', encoding='utf8')
    for line in inf:
        ls_line = set(re.findall("[\w]+", line.lower()))
       # print("ls_line", ls_line)
        intersection = ls_line.intersection(searched_words)
        #print("intersection", intersection)
        if len(intersection) != 0:
            ouf.write(line)

print("Finished.")

inf.close()
ouf.close()
words_file.close()
