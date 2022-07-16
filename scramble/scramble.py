import itertools

class Scramble:

	def __init__(self, dictionary: list) -> None:
		self.dictionary_list = dictionary
		self.scrambles = []
		self.matches = 0

		for d in self.dictionary_list:
			self.scrambles.extend(self.generateScrambles(d))

		self.orchistrate_generated_scrambles()

	def get_matches(self, longString: str)-> int:
		for d in self.dictionary_list:
			if d in longString:
				self.matches = self.matches + 1
		return self.matches

	def generateScrambles(self, dictionary: str)-> list:
		scrambles = []
		permutations = list(map("".join, itertools.permutations(dictionary)))
		for p in permutations:
				if (p[0] == dictionary[0] and p[-1] == dictionary[-1]):
					scrambles.append(p)
		return scrambles

	def orchistrate_generated_scrambles(self)-> None:
		#remove duplicates
		self.scrambles = list(dict.fromkeys(self.scrambles))
		#merge scrumble list into the dictionary list
		self.dictionary_list = itertools.chain(self.dictionary_list, self.scrambles)
