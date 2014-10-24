import re
__author__ = 'adm'

file = open("test_en.txt", 'r')
file_of_words = open("list_of_words.txt", 'w')
text = file.read()

class TextSplitter:
    def __init__(self, delimiters = ' ,.()!?;:\/*=+-'):
        self.delimiters = delimiters

    def split_by_spaces(self, text):
        list_of_words = text.split()
        return list_of_words

    def split_into_words(self, text):
        return re.findall("[a-zA-Z]+", text)

    def split_into_words_and_numbers(self, text):
        return re.findall("[\w]+", text)

    def split_into_words2(self, text):
        return re.split("["+ self.delimiters + "]+", text)

    def split_into_words3(self, text):
        modified_text = text
        for delimiter in self.delimiters:
            modified_text = modified_text.replace(delimiter, " ")
        list_of_words = modified_text.split()
        return list_of_words


splitter = TextSplitter()
list_of_words = splitter.split_into_words(text)
dict_of_words = {}

for word in list_of_words:
    word = word.lower()
    if word in dict_of_words:
       dict_of_words[word] +=1
    else:
        dict_of_words[word] = 1

for word in sorted(dict_of_words):
    words = str(word) + " " + str(dict_of_words[word]) + "\n"
    file_of_words.write(words)

#words = "\n".join(list_of_words)
file_of_words.write(words)

file.close()
file_of_words.close()
