__author__ = 'YKolotolova'

from splitting_text_into_ngramms import *

# file = open("test_en.txt", 'r')
# file_of_words = open("list_of_words.txt", 'w')
# text = file.read()
#
# splitter = TextSplitter()
# list_of_words = splitter.split_into_words(text)


class FrequencyCounter:
    def count_words(self, list_of_words):
        dict_of_words = {}
        for word in list_of_words:
            word = word.lower()
            if word in dict_of_words:
               dict_of_words[word] +=1
            else:
                dict_of_words[word] = 1
        words = '' #убрать, когда буду писать в файл, также убрать += в цикле ниже и return words
        for word in sorted(dict_of_words):
            words += str(word) + " " + str(dict_of_words[word]) + "\n"
#             file_of_words.write(words)
        return words

# word_counter = FrequencyCounter()
# print(word_counter.count_words(list_of_words))

# file.close()
# file_of_words.close()
