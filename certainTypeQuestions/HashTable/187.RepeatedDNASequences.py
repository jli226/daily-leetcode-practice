# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# Example:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

# Output: ["AAAAACCCCC", "CCCCCAAAAA"]


class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dictionary = dict()
        for i in [s[x: x + 10] for x in range(len(s) - 9)]:
            dictionary[i] = dictionary.get(i, 0) + 1
        return [k for k, v in dictionary.iteritems() if v > 1]
