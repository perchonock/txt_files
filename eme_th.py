import re

inf = open("nums.txt", 'r', encoding="utf8")
ouf = open("nums4replacement.txt", 'w', encoding="utf8")

for line in inf:
    nums_in_line = re.findall('[0-9]+', line.strip())
    num = nums_in_line[0]
    if num.endswith('11') or num.endswith('12') or num.endswith('13'):
        s = line.strip('\n') + '\t' + " " + num + "th " + '\n'
        ouf.write(s)
    elif num.endswith('1'):
        s = line.strip('\n') + '\t' + " " + num + "st " + '\n'
        ouf.write(s)
    elif num.endswith('2'):
        s = line.strip('\n') + '\t' + " " + num + "nd " + '\n'
        ouf.write(s)
    elif num.endswith('3'):
        s = line.strip('\n') + '\t' + " " + num + "rd " + '\n'
        ouf.write(s)
    else:
        s = line.strip('\n') + '\t' + " " + num + "th " + '\n'
        ouf.write(s)

print('done!')

inf.close()
ouf.close()
