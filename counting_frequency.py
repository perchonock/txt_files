__author__ = 'YKolotolova'

from splitting_text_into_ngramms import *

file = open("h.txt", 'r', encoding='utf-8')
file_of_words = open("list_of_words.txt", 'w', encoding='utf-8')
text = file.read()

splitter = TextSplitter()
list_of_words = splitter.split_into_words(text)

def get_item(a):
    def get_i(pair):
        return pair[a]
    return get_i

class FrequencyCounter:
    def count_words(self, list_of_words):
        dict_of_words = {}
        for word in list_of_words:
            word = word.lower()
            if word in dict_of_words:
               dict_of_words[word] +=1
            else:
                dict_of_words[word] = 1
        return dict_of_words

    def sort_by_frequency(self, dict_of_words):
        words = ''
        for key_value in sorted(dict_of_words.items(), key = get_item(1), reverse = True):
            words += key_value[0] + " " + str(key_value[1]) + "\n"
        return words

    def sort_by_alph(self, dict_of_words):
        words = ''
        for key_value in sorted(dict_of_words.items()):
            words += key_value[0] + " " + str(key_value[1]) + "\n"
        return words

word_counter = FrequencyCounter()
dict = word_counter.count_words(list_of_words)
print(word_counter.sort_by_alph(dict))

file.close()
file_of_words.close()


def foreach(collection, function):
    for a in collection:
        function(a)

lst = [1,2,4,5,6]

def printSquare(value):
    print(value*value)


#foreach(lst, printSquare)

def reduce(collection, function, zeroElement):
    result = zeroElement
    for a in collection:
        result = function(a, result)
    return result

def sum(a, b):
    return a + b

print(reduce(lst, lambda a,b:  a + b, 0))

print(reduce(lst, lambda a,b:  a * b, 1))