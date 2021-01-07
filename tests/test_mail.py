
#!/c/Anaconda3/envs/myenv/python
import sys
import unittest
import datetime as dt

from modules import modules

class TestGreetingsWord(unittest.TestCase):
    
    def test_time_of_day(self):
        # Define pair time-greeting_word values to run the test on
        time_expected = [(22, 'Good night'), (0, 'Good night'), (3, 'Good night'),
                (9, 'Good morning'), (14, 'Good afternoon'), (19, 'Good evening')]
                
        for time, greeting in time_expected:
            with self.subTest(input_pair=(time, greeting)):
                self.assertEqual(modules.get_greetings_word(dt.time(time)), greeting)
    
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