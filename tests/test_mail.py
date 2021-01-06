
#!/c/Anaconda3/envs/myenv/python
import sys
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
    
class TestTimeConversion(unittest.TestCase):
    
    def test_complete_hrs_type(self):
        test_case = 120*60 # seconds
        out = map(type, modules.get_hrs_mins(test_case))
        expected = (int, int)
        self.assertEqual(tuple(out), expected)

    def test_complete_hrs_1(self):
        test_case = 120*60 # seconds
        expected = (2, 0)
        self.assertEqual(modules.get_hrs_mins(test_case), expected)
    
    def test_complete_hrs_2(self):
        test_case = 130*60 # seconds
        expected = (2, 10)
        self.assertEqual(modules.get_hrs_mins(test_case), expected)


if __name__ == "__main__":      
    unittest.main()