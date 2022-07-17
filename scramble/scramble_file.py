from pathlib import Path
from file_handler import FileHandler

BASE_DIR = Path(__file__).resolve().parent.parent

class ScrambleFile(FileHandler):
    dictionary_file = "dictionary.dict"
    input_file = "input.dict"
    CONST_MAX_DICTIONARY_LENGTH = 105
    CONST_MIN_DICTIONARY_LENGTH = 2

    dictionary_data = []
    input_data = []

    def __init__(self, directory: str = "")-> None:
        super().__init__(BASE_DIR / "scramble")
        super().open(self.dictionary_file)
        self.dictionary_data = self.to_list()
        self.file.close()
        super().open(self.input_file)
        self.input_data = self.to_list()
        self.file.close()
        self.limitations()

    def limitations(self):
        if len(self.dictionary_file) > self.CONST_MAX_DICTIONARY_LENGTH:
            raise ValueError("A dictionary value has exceeded the limit")

        for d in self.dictionary_data:
            if len(d) < self.CONST_MIN_DICTIONARY_LENGTH or len(d) > self.CONST_MAX_DICTIONARY_LENGTH:
                raise ValueError("Dictionary value not in the specified range")