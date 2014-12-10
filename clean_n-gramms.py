import sys
import re

in_file = sys.argv[1]
inf = open(in_file, "r", encoding='utf8')
ouf = open(re.sub("\.txt", "", in_file) + "_clean.txt", 'w', encoding='utf16')
deleted = open(re.sub("\.txt", "", in_file) + "_deleted.txt", "w", encoding='utf16')

punc_marks = '!@():"?\/;,.='
punc_marks = set(punc_marks)
stop_words = {'de', 'la', 'du', 'des', 'le', 'les', 'un', 'une', 'sur', '\u00e0', 'au', 'aux', 'pour', 'et', 'ou', 'par',
                   'dans', 'pas', 'sous'}

for line in inf:
    line_set = set(line.strip())
    ls_line = line.lower().split()
    intersection = line_set.intersection(punc_marks)
    if len(intersection) == 0 and ls_line[0] not in stop_words and ls_line[-2] not in stop_words:
        ouf.write(line)
    else:
        deleted.write(line)

print("Finished")

inf.close()
ouf.close()
deleted.close()


