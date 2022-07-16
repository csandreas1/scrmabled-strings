import unittest
from scramble import Scramble

class TestingScramble(unittest.TestCase):
    def test_generate_scrambles(self):
        scramble = Scramble()
        scrambled_list = scramble.generateScrambles("this")
        self.assertEqual(scrambled_list, ["this", "tihs"])

    def test_generate_scrambles_2(self):
        scramble = Scramble()
        scrambled_list = scramble.generateScrambles("bath")
        self.assertEqual(scrambled_list, ["bath", "btah"])

    def test_generate_scrambles_3(self):
        scramble = Scramble()
        scrambled_list = scramble.generateScrambles("pool")
        self.assertEqual(scrambled_list, ["pool", "pool"])


    def test_get_matches(self):
        scramble = Scramble(["axpaj", "apxaj", "dnrbt", "pjxdn", "abd"])
        matches = scramble.get_matches("aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt")
        self.assertEqual(matches, 4)

    def test_get_matches_2(self):
        scramble = Scramble(["axpaj", "apxaj", "dnrbt", "pjxdn", "abd", "pool"])
        matches = scramble.get_matches("aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbtpool")
        self.assertEqual(matches, 6)

if __name__ == "__main__":
    unittest.main()
