
import sys
sys.path.insert(1, 'C:/Users/KostaGeo/Desktop/send-mail-py_operational')
import unittest
from modules import modules
import datetime as dt

class TestGreetingsWord(unittest.TestCase):
    def test_night_1(self):
        test_case = dt.time(22)
        expected = 'Good night'
        self.assertEqual(modules.get_greetings_word(test_case), expected)
    
    def test_night_2(self):
        test_case = dt.time(0)
        expected = 'Good night'
        self.assertEqual(modules.get_greetings_word(test_case), expected)
    
    def test_night_3(self):
        test_case = dt.time(3)
        expected = 'Good night'
        self.assertEqual(modules.get_greetings_word(test_case), expected)
    
    def test_morning(self):
        test_case = dt.time(9)
        expected = 'Good morning'
        self.assertEqual(modules.get_greetings_word(test_case), expected)
    
    def test_afternoon(self):
        test_case = dt.time(14)
        expected = 'Good afternoon'
        self.assertEqual(modules.get_greetings_word(test_case), expected)

    def test_evening(self):
        test_case = dt.time(19)
        expected = 'Good evening'
        self.assertEqual(modules.get_greetings_word(test_case), expected)
    

if __name__ == "__main__":      
    unittest.main()