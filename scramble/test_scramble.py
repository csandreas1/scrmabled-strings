import unittest
from scramble import Scramble

class TestingScramble(unittest.TestCase):

    def test_get_matches(self):
        scramble = Scramble(["axpaj", "apxaj", "dnrbt", "pjxdn", "abd"])
        matches = scramble.get_matches("aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt")
        self.assertEqual(matches, 4)

    def test_get_matching_scrambles(self):
        scramble = Scramble(["axpaj", "apxaj", "dnrbt", "pjxdn", "abd", "whatever"])
        scramble.get_matches("aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt")

        self.assertEqual(scramble.scrambles, ["axpaj", "apxaj", "dnrbt", "pjxdn"])

    def test_get_matching_scrambles_2(self):
        scramble = Scramble(["sparta", "spatra", "this", "whatever"])
        scramble.get_matches("thisissparta")

        self.assertEqual(scramble.scrambles, ["sparta", "spatra", "this"])


if __name__ == "__main__":
    unittest.main()