# Import all required modules

import unittest
import sys
sys.path.insert(1, '/home/timothy/matrix-week-three/src')

import email_parser

class TestEmailParser(unittest.TestCase):
    def setUp(self):
        self.test_case = email_parser.EmailParser()

    def test_first_parse(self): 
        self.assertEqual(self.test_case.parse('timothyabiodun@gmail.com'), {'domain': 'gmail.com', 'username': 'timothyabiodun'})
        
    def test_second_parse(self):
        self.assertEqual(self.test_case.parse('3timothyabiodun@gmail.com'), None)
    
    def test_third_parse(self):
        self.assertEqual(self.test_case.parse('timothy-abiodun@gmail.com'), None)
    
    def test_fourth_parse(self):
        self.assertEqual(self.test_case.parse('timothy400@yahoo.com'), {'username': 'timothy400', 'domain': 'yahoo.com'})

    def test_fifth_parse(self):
        self.assertEqual(self.test_case.parse('timothyabiodun3@hotmail.com'), {'username': 'timothyabiodun3', 'domain': 'hotmail.com'})

    def test_sixth_parse(self):
        self.assertEqual(self.test_case.parse('#timothyabiodun@gmail.com'), None)

    def test_seventh_parse(self):
        self.assertEqual(self.test_case.parse(' timothyabiodun@yahoo.com'), None)

    def test_eighth_parse(self):
        self.assertEqual(self.test_case.parse('timothyabiodun@gmail.2com'), None)

    def test_ninth_parse(self):
        self.assertEqual(self.test_case.parse('timothyabiodun@yahoo.com2'), None)

    def test_tenth_parse(self):
        self.assertEqual(self.test_case.parse('jane+doe@gmail.com'), {'username': 'jane+doe', 'domain': 'gmail.com'})



if __name__ == '__main__':
    unittest.main()
