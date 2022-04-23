import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


unittest.main()