from scramble import Scramble
from scramble_file import ScrambleFile
import logging

logging.basicConfig(filename='logging.log',format='%(asctime)s %(message)s', encoding='utf-8', level=logging.DEBUG)

def execute():
    logging.info("Execution started...")
    scramble_file = ScrambleFile()
    scramble = Scramble(scramble_file.dictionary_data)

    c = 0
    for i in scramble_file.input_data:
        if scramble.get_matches(i) > 0:
            c += 1
            print(f"Case #{c}: {str(scramble.matches)}")

    logging.info("Execution ended successfully...")

execute()
