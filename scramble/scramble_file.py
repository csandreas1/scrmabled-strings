from pathlib import Path
from file_handler import FileHandler

BASE_DIR = Path(__file__).resolve().parent.parent

class ScrambleFile(FileHandler):
    dictionary_file = "dictionary.dict"
    input_file = "input.dict"

    dictionary_data = []
    input_data = []

    def __init__(self, directory: str = "") -> None:
        super().__init__(BASE_DIR / "scramble")
        super().open(self.dictionary_file)
        self.dictionary_data = self.to_list()
        self.file.close()
        super().open(self.input_file)
        self.input_data = self.to_list()
        self.file.close()