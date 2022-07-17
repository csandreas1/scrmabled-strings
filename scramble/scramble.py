import itertools
import logging
import logging.config

class Scramble:
	def __init__(self, dictionary: list = [])-> None:
		self.dictionary_list = dictionary
		self.matches = 0
		self.anagrams = {}
		self.scrambles = []
		logging.info("Dictionary List:")
		logging.debug(self.dictionary_list)

	def is_anagram(self, str1, str2)-> bool:
		lettercount = len(str1)
		if lettercount not in self.anagrams:
			# build the list for that letter length
			self.anagrams[lettercount] = [sorted(str2[x:x+lettercount]) for x in range(len(str2)-lettercount)]
		return (sorted(str1) in self.anagrams[lettercount])

	def get_matches(self, long_string: str)-> int:
		self.matches = 0
		for l in self.dictionary_list:
			if self.is_anagram(l, long_string):
				self.scrambles += [l]
				self.matches += 1

		logging.info(f"{self.matches} matches found for input '{long_string}'")
		logging.debug(self.scrambles)
		return self.matches
