import itertools
import logging
import logging.config

class Scramble:
	def __init__(self, dictionary: list = [])-> None:
		self.dictionary_list = dictionary
		self.scrambles = []
		self.dictionary_with_scrambles = []
		self.matches = 0
		logging.info("Dictionary List:")
		logging.debug(self.dictionary_list)

		for d in self.dictionary_list:
			self.scrambles.extend(self.generateScrambles(d))

		logging.info("Generated scrambles:")
		logging.debug(self.scrambles)

		self.orchistrate_generated_scrambles()

		logging.info("Dictionary list with scrambles: ")
		logging.debug(self.dictionary_with_scrambles)

	def get_matches(self, longString: str)-> int:
		self.matches = 0
		matches = []
		dictionary_scrambles_advanced = list(map(self.get_first_and_last_character, self.dictionary_with_scrambles))
		# COMMENT: 'axpaj' is not matching in its scrumbled version 'aapxj'...
		#This is wrong
		for d in self.dictionary_with_scrambles:
			if d in longString:
				self.matches += 1
				matches.append(d)
				#check for scrambled matches
				for data in dictionary_scrambles_advanced:
					if data[0] in self.dictionary_list \
						and data[0] not in matches \
							and (d[0] + d[-1] == data[1] and len(d) == data[2]):
						self.matches += 1
						matches.append(data[0])


		logging.info(f"{self.matches} matches found for input '{longString}'")
		logging.debug(matches)
		return self.matches

	def generateScrambles(self, dictionary: str)-> list:
		scrambles = []
		permutations = list(map("".join, itertools.permutations(dictionary)))
		for p in permutations:
				if p not in self.dictionary_list and (
					p[0] == dictionary[0] and p[-1] == dictionary[-1]
				):
					scrambles.append(p)
		return scrambles

	def orchistrate_generated_scrambles(self)-> None:
		#remove duplicates
		self.scrambles = list(dict.fromkeys(self.scrambles))
		#merge scrumble list into the dictionary list
		self.dictionary_with_scrambles = list(itertools.chain(self.dictionary_list, self.scrambles))

	def get_first_and_last_character(self, string:str)-> list:
		return [string, string[0] + string[-1], len(string)]