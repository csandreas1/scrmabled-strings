import unittest
from scramble_file import ScrambleFile

class TestingScrambleFileData(unittest.TestCase):
    def test_can_open_and_read_dictionary_file_as_list(self):
        scramble_file.open("dictionary.dict")
        dictionary_data = scramble_file.to_list()
        self.assertIsInstance(dictionary_data, list)
        scramble_file.file.close()

    def test_can_open_and_read_input_file_as_list(self):
        scramble_file.open("input.dict")
        input_data = scramble_file.to_list()
        self.assertIsInstance(input_data, list)
        scramble_file.file.close()

if __name__ == '__main__':
    scramble_file = ScrambleFile()
    unittest.main()
