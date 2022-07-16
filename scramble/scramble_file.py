from file.file import File


class ScrambleFile(File):
    def __init__(self, directory: str = "") -> None:
        super().__init__(directory)