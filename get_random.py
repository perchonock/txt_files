'''
Запускать следующим образом:
название_скрипта название_файла количество_строк
название_файла - название файла, из которого  нужно извлчечь случайные строки. Должен быть в кодировке utf8 без BOM.
количество_строк - желаемое кол-во строк в итоговом файле
'''

import sys
import re
import random

#in_file = sys.argv[1]
#n = int(sys.argv[2])
in_file = 'vtb_requests.txt'
n = 10000

inf = open(in_file, "r", encoding='utf8')
ouf = open(re.sub("\.txt", "", in_file) + "_random" + str(n) + ".txt", 'w', encoding='utf8')

lines_ls = []
for line in inf:
    if line.strip() != '':
        lines_ls.append(line.strip())

if n > len(lines_ls):
    n = len(lines_ls)

random_lines = random.sample(lines_ls, n)

for i, key in enumerate(random_lines):
    if i != n-1:
        ouf.write(key + "\n")
    else:
        ouf.write(key)

print("Finished")

inf.close()
ouf.close()


