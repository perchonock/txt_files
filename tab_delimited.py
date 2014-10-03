__author__ = 'YKolotolova'
file1 = open("test1.txt", 'r')
file2 = open("test2.txt", 'r')
file_merged = open("test_tab_delimited.txt", 'w')

#num_lines = sum(1 for line in file1) - считает количество строк в файле.
#print(num_lines)
#после добавления этого кода, последующий с if начинает работать неправильно. почему? хотя число строк получается правильным.
#файл подвергается изменениям?! он не может, т.к. мы только читаем.

for i in range(0,10):
#while file1.readline != "":
#читает файл бесконечно. почему? тут https://docs.python.org/3.4/tutorial/inputoutput.html написано, что, когда достигается
#конец файл, эта функция возвращает пустую строку.
    new_line = file1.readline().rstrip('\n') + "\t" + file2.readline()
    print(new_line)
    file_merged.write(new_line)

file1.close()
file2.close()
file_merged.close()
