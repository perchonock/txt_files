import sys
import re
import random

in_file = sys.argv[1]
inf = open(in_file, "r", encoding='utf8')
ouf = open(re.sub("\.txt", "", in_file) + "_random.txt", 'w', encoding='utf8')

for line in inf:
    rand_num = random.randrange(0,10)
    if rand_num == 1:
        ouf.write(line)

print("Finished")

inf.close()
ouf.close()


