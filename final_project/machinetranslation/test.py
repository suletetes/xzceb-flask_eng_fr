import unittest
from translator import english_to_french, french_to_english


class testing_english_to_french(unittest.TestCase):
    def testing(self):
        self.assertEqual(english_to_french('apple'), 'pomme')  # "apple" -> "pomme"
        self.assertNotEqual(english_to_french('apple'), 'pomme')  # "apple" -> "pomme"
        # self.assertEqual(english_to_french(None), None)


class testing_to_french_to_english(unittest.TestCase):
    def testing(self):
        self.assertEqual(french_to_english('pomme'), 'apple')  # "apple" -> "pomme"
        self.assertNotEqual(french_to_english('pomme'), 'apple')  # "apple" -> "pomme"
        # self.assertEqual(french_to_english(None), None)


unittest.main()
