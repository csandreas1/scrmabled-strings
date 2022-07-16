import itertools
import logging
import logging.config

class Scramble:
	def __init__(self, dictionary: list = [])-> None:
		self.dictionary_list = dictionary
		self.scrambles = []
		self.matches = 0
		logging.info("Dictionary List:" )
		logging.debug(self.dictionary_list)

		for d in self.dictionary_list:
			self.scrambles.extend(self.generateScrambles(d))

		logging.info("Generated scrambles:" )
		logging.debug(self.dictionary_list)

		self.orchistrate_generated_scrambles()

		logging.info("Dictionary has been merged with non-duplicated scrambles: " )
		logging.debug(self.dictionary_list)

	def get_matches(self, longString: str)-> int:
		self.matches = 0
		list = []
		for d in self.dictionary_list:
			if d in longString:
				self.matches += 1
				list.append(d)
		logging.info(f"{self.matches} matches found for input {longString}")
		logging.debug(list)
		return self.matches

	def generateScrambles(self, dictionary: str)-> list:
		permutations = list(map("".join, itertools.permutations(dictionary)))
		for p in permutations:
				if (p[0] == dictionary[0] and p[-1] == dictionary[-1]):
					self.scrambles.append(p)
		return self.scrambles

	def orchistrate_generated_scrambles(self)-> None:
		#remove duplicates
		self.scrambles = list(dict.fromkeys(self.scrambles))
		#merge scrumble list into the dictionary list
		self.dictionary_list = list(itertools.chain(self.dictionary_list, self.scrambles))
