from random import shuffle
import itertools
import pprint
"""
If the length of the string is 1, stop.
If the length of the string is > 1, do the following:
Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
Apply step 1 recursively on each of the two substrings x and y.
Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
"""

# Todo: __init__: for each dictionary append to the list its scrambled version

def isMatch(dictionary: list, longString: str) -> bool:

    if longString in dictionary:
        return True
    return False

def generateScrambles(dictionary: list) ->list:

    scrambles = dictionary
    for d in dictionary:
        permutations = list(map("".join, itertools.permutations(d)))

        for p in permutations:
                if d != p and (p[0] == d[0] and p[-1] == d[-1]):
                    scrambles.append(p)
    return scrambles

dictionary_list = ['axpaj', 'apxaj', 'dnrbt', 'pjxdn', 'abd']

# r = isScramble(dictionary_list, 'aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt')

# print(r)

print(generateScrambles(['this', 'pjxdn']))