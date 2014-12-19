__author__ = 'YKolotolova'

import sys
import re

in_file = sys.argv[1]
list_of_words = sys.argv[2]
# in_file = 'text_only.txt.001'
# list_of_words = "ina_unknown.txt"
inf = open(in_file, "r", encoding='utf8')
ouf = open(re.sub("\.txt", "", in_file) + "_contexts.txt", 'w', encoding='utf16')
words_file = open(list_of_words, "r", encoding='utf8')

searched_words = set()
for line in words_file:
    searched_words.add(line.strip().lower())

#print("searched words", searched_words)

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
