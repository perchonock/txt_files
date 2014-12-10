import sys
import re

in_file = sys.argv[1]
inf = open(in_file, "r")
ouf = open(re.sub("\.txt", "", in_file) + "_no_punctuation.txt", 'w')
deleted = open(re.sub("\.txt", "", in_file) + "deleted_punctuation.txt", "w")
punc_marks = '!@():"?\/;,.='
punc_marks = set(punc_marks)

for line in inf:
    line_set = set(line.strip())
    intersection = line_set.intersection(punc_marks)
    if len(intersection) == 0:
        ouf.write(line)
    else:
        deleted.write(line)

print("Finished")

inf.close()
ouf.close()
deleted.close()



