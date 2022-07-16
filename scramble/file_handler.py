from typing import Iterator


class FileHandler:
    def __init__(self, directory: str = "")-> None:
        self.data = []
        self.file = None
        self.directory = directory

    def open(self, file_name: str)-> Iterator:
        self.file = open(self.directory / file_name, "r")
        return self.file

    def to_list(self)-> list:
        self.data = self.file.read().splitlines()
        return self.data