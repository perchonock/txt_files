import sys
import re

in_file = sys.argv[1]
#in_file = 'test_stop.txt'
inf = open(in_file, "r", encoding='utf8')
ouf = open(re.sub("\.txt", "", in_file) + "_clean.txt", 'w', encoding='utf16')
deleted = open(re.sub("\.txt", "", in_file) + "_deleted.txt", "w", encoding='utf16')
stop_words = {'de', 'la', 'du', 'des', 'le', 'les', 'un', 'une', 'sur', '\u00e0', 'au', 'aux', 'pour', 'et', 'ou', 'par',
                   'dans', 'pas', 'sous'}

for line in inf:
    ls_line = line.lower().split()
    if ls_line[0] in stop_words or ls_line[-2] in stop_words:
        deleted.write(line)
    else:
        ouf.write(line)

print("Finished.")

inf.close()
ouf.close()
deleted.close()
