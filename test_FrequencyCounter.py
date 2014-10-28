from unittest import TestCase
from counting_frequency import *

__author__ = 'YKolotolova'


class TestFrequencyCounter(TestCase):
    def test_count_words(self):
        lst_of_words = ['table', 'chair', 'table', 'bla', 'new', 'table']
        word_counter = FrequencyCounter()
        words = word_counter.count_words(lst_of_words)
        words2 = 'bla 1\nchair 1\nnew 1\ntable 3\n'
        self.assertTrue(words == words2, 'strings are not the same')
