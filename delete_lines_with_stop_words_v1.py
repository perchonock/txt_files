__author__ = 'YKolotolova'

import sys
import re

in_file = sys.argv[1]
inf = open(in_file, "r")
ouf = open(re.sub("\.txt", "", in_file) + "_clean.txt", 'w')
deleted = open(re.sub("\.txt", "", in_file) + "_deleted.txt", "w")
words_to_delete = {'de', 'la', 'du', 'des', 'le', 'les', 'un', 'une', 'sur', 'a', 'au', 'aux', 'pour', 'et', 'ou', 'par',
                   'dans', 'pas', 'sous'}

for line in inf:
    stripped_line = re.sub(" [0-9]+$", '', line).strip()
    found = False
    for word in words_to_delete:
        if line.lower().startswith(word + " ") or stripped_line.lower().endswith(" " + word):
            deleted.write(line)
            found = True
            break
    if not found:
        ouf.write(line)

print("Finished.")

inf.close()
ouf.close()
deleted.close()
