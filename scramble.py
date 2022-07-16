import itertools
import pprint

print("running...")
# Todo: __init__: for each dictionary append to the list its scrambled version

def isMatch(dictionary: list, longString: str)-> bool:
    if longString in dictionary:
        return True
    return False

def generateScrambles(dictionary: str)-> list:
	scrambles = []
	permutations = list(map("".join, itertools.permutations(dictionary)))
	for p in permutations:
			if (p[0] == dictionary[0] and p[-1] == dictionary[-1]):
				scrambles.append(p)
	return scrambles


dictionary_list = ['axpaj', 'apxaj', 'dnrbt', 'pjxdn', 'abd']

# r = isScramble(dictionary_list, 'aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt')

# print(r)

print(generateScrambles('this'))
print("Completed")