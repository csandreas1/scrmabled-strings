from pathlib import Path
from file_handler import FileHandler

BASE_DIR = Path(__file__).resolve().parent.parent

class ScrambleFile(FileHandler):
    def __init__(self, directory: str = "") -> None:
        super().__init__(BASE_DIR / "scramble")
