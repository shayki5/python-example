from count_words_chars import longest_word
import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertGreater(longest_word('/home/test.txt'), 9999)

if __name__ == '__main__':
    unittest.main()