import unittest
from scramble import Scramble

class TestingScramble(unittest.TestCase):

    def test_get_matches(self):
        scramble = Scramble(["axpaj", "apxaj", "dnrbt", "pjxdn", "abd"])
        matches = scramble.get_matches("aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt")
        self.assertEqual(matches, 4)

    def test_get_result(self):
        scramble = Scramble(["axpaj", "apxaj", "dnrbt", "pjxdn", "abd", "whatever"])
        scramble.get_matches("aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt")

        self.assertEqual(scramble.scrambles, ["axpaj", "apxaj", "dnrbt", "pjxdn"])

if __name__ == "__main__":
    unittest.main()