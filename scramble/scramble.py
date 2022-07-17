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
		letter_length = len(str1)
		cachekey = (str2, str1)
		if cachekey not in self.anagrams:
			# build the list for that letter length
			self.anagrams[cachekey] = [sorted(str2[x:x+letter_length]) for x in range(len(str2)-letter_length+1)]
		return (sorted(str1) in self.anagrams[cachekey])

	def get_matches(self, long_string: str)-> int:
		self.matches = 0
		self.scrambles = []

		for l in self.dictionary_list:
			if self.is_anagram(l, long_string):
				self.scrambles += [l]
				self.matches += 1

		logging.info(f"{self.matches} matches found for input '{long_string}'")
		logging.debug(self.scrambles)
		return self.matches
