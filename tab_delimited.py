__author__ = 'YKolotolova'
file1 = open("test1.txt", 'r')
file2 = open("test2.txt", 'r')
file_merged = open("test_tab_delimited.txt", 'w')

#num_lines = sum(1 for line in file1) # считает количество строк в файле.
#print(num_lines)
#file1.seek(0) - #сбрасывает номер строки файла на начальную

for file1_line in file1:
    new_line = (file1_line.rstrip('\n') + "\t" + file2.readline().rstrip('\n')) + '\n'
    print(new_line)
    file_merged.write(new_line)


#file1_line = file1.readline()
#while file1_line != "":
#    new_line = (file1_line.rstrip('\n') + "\t" + file2.readline().rstrip('\n')) + '\n'
#    print(new_line)
#    file_merged.write(new_line)
#    file1_line = file1.readline()



file1.close()
file2.close()
file_merged.close()
