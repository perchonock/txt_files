import re
__author__ = 'adm'

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

