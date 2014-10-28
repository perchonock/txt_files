from unittest import TestCase
from splitting_text_into_ngramms import *

__author__ = 'adm'


class TestTextSplitter(TestCase):
    def test_split_by_spaces(self):
        lst = ["a", "r", "c", "d", "e"]
        text = " ".join(lst)
        splitter = TextSplitter()
        lst2 = splitter.split_by_spaces(text)
        self.assertTrue(lst == lst2, "you're wrong bitch!")

    def test_split_by_dot(self):
        lst = ["a", "r", "c", "d", "e"]
        text = ".".join(lst)
        splitter = TextSplitter()
        lst2 = splitter.split_into_words(text)
        self.assertTrue(lst == lst2, "you're wrong bitch!")

    def test_split_by_comma(self):
        lst = ["a", "r", "c", "d", "e"]
        text = ", ".join(lst)
        splitter = TextSplitter()
        lst2 = splitter.split_into_words(text)
        self.assertTrue(lst == lst2, "you're wrong bitch!")

    def test_super_split(self):
        lst = ["a", "r", "cg", "dg", "e", "a", "r", "c", "dd", "de", "a", "r", "c", "d", "e"]
        delimeters = ' ,.()!?;:\\\/*=+-'
        testString = ""
        for firstIndex in range(0, len(lst)):
            secondIndex = firstIndex % len(delimeters)
            testString += lst[firstIndex]
            if(firstIndex != len(lst) - 1):
                testString += delimeters[secondIndex]
        splitter = TextSplitter(delimeters)
        lst2 = splitter.split_into_words(testString)
        self.assertTrue(lst == lst2, str(lst2))
