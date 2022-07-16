class File:
    def __init__(self, directory: str = "") -> None:
        self.file = None
        self.directory = directory
        self.data = []

    def open(self, file_name: str)-> None:
        self.file = open(self.directory / file_name, "r")

    def read(self)-> None:
        self.data = self.data.read()

    def read_lines(self)-> None:
        self.data = self.data.readlines()

    def close(self)-> None:
        self.file.close()
