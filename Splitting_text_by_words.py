import re
__author__ = 'adm'

class TextSplitter:
    def __init__(self, delimiters = ' ,.()!?;:\/*=+-'):
        self.delimiters = delimiters

    def split_by_spaces(self, text):
        list_of_words = text.split()
        return list_of_words

    def split2(self, text):
        modified_text = text
        for delimiter in self.delimiters:
            modified_text = modified_text.replace(delimiter, " ")
        list_of_words = modified_text.split()
        return list_of_words

    def split(self, text):
        return re.split("["+ self.delimiters + "]+", text)


#print(re.split("["+ " ,.()!?;:\\/*=+-" + "]+", "text ,ffsd ,. pron,.ff push me touch me ...(satisfaction)"))


#a = 'abc'
#print("(" + a + ")")


