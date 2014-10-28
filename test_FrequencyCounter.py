from unittest import TestCase
from counting_frequency import *

__author__ = 'YKolotolova'


class TestFrequencyCounter(TestCase):
    def test_count_words1(self):
        lst_of_words = ['table', 'chair', 'table', 'bla', 'new', 'table']
        word_counter = FrequencyCounter()
        words = word_counter.count_words(lst_of_words)
        words2 = 'bla 1\nchair 1\nnew 1\ntable 3\n'
        self.assertTrue(words == words2, words)

    def test_count_words2(self):
        lst_of_words = []
        word_counter = FrequencyCounter()
        words = word_counter.count_words(lst_of_words)
        words2 = ''
        self.assertTrue(words == words2, words)
