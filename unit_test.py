from count_words_chars import longest_word
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertGreater(longest_word('/home/shayki/test.txt'), 9)

if __name__ == '__main__':
    unittest.main()