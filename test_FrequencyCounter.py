from unittest import TestCase
from counting_frequency import *

__author__ = 'YKolotolova'


class TestFrequencyCounter(TestCase):
    def test_count_words1(self):
        lst_of_words = ['table', 'chair', 'table', 'bla', 'new', 'table', 'chair', 'new', 'new', 'table']
        word_counter = FrequencyCounter()
        words = word_counter.count_words(lst_of_words)
        words2 = 'table 4\nnew 3\nchair 2\nbla 1\n'
        self.assertTrue(words == words2, words)
#написать тест, который проверяет только функцию подсчета слов. Например, просерить, что размер возвращаемого словаря правильный,
    #содержит все слова, слова с правильным значением частоты
    def test_count_words2(self):
        lst_of_words = []
        word_counter = FrequencyCounter()
        words = word_counter.count_words(lst_of_words)
        words2 = ''
        self.assertTrue(words == words2, words)
