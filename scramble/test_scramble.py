import unittest
from scramble import Scramble

class TestingScramble(unittest.TestCase):
    def test_generate_scrambles(self):
        scrambled_list = scramble.generateScrambles("this")
        self.assertEqual(scrambled_list, ["this", "tihs"])

    def test_get_matches(self):
        matches = scramble.get_matches("aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt")
        self.assertEqual(matches, 4)

if __name__ == '__main__':
    scramble = Scramble(['axpaj', 'apxaj', 'dnrbt', 'pjxdn', 'abd'])
    unittest.main()
