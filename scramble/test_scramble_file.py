import unittest
from scramble_file import ScrambleFile

class TestingScrambleFile(unittest.TestCase):
    def test_can_open(self):
        scramble_file.open("dictionary.dict")
        scramble_file.read_lines()

        self.assertEqual(type(self.data), "list")

if __name__ == '__main__':
    scramble_file = ScrambleFile()
    unittest.main()
