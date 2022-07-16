import unittest
from scramble import Scramble

class TestingScramble(unittest.TestCase):

    def test_generate(self):
        scrambled_string = Scramble.generateScrambles("this")
        self.assertEqual(scrambled_string, ["this", "tihs"])

if __name__ == '__main__':
    unittest.main()