from scramble import Scramble
from scramble_file import ScrambleFile



def execute():
    scramble_file = ScrambleFile()
    scramble_file.open(scramble_file.dictionary_file)
    dictionary_file_list = scramble_file.to_list()

    scramble = Scramble(dictionary_file_list)

    scramble_file.file.close()

    ScrambleFile().__init__()

    scramble_file.open(scramble_file.input_file)
    input_file_list = scramble_file.to_list()
    scramble_file.file.close()

    c = 0
    for i in input_file_list:
        if scramble.get_matches(i) > 0:
            c += 1
            print(f"Case #{c}: {str(scramble.matches)}")


execute()
