# 521. Longest Uncommon Subsequence I
# Easy

# 269

# 4026

# Add to List

# Share
# Given two strings, you need to find the longest uncommon subsequence of this two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other string.

# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

# The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.


# Example 1:

# Input: a = "aba", b = "cdc"
# Output: 3
# Explanation: The longest uncommon subsequence is "aba",
# because "aba" is a subsequence of "aba",
# but not a subsequence of the other string "cdc".
# Note that "cdc" can be also a longest uncommon subsequence.
# For strings A, B, when len(A) > len(B), the longest possible subsequence of either A or B is A, and no subsequence of B can be equal to A. Answer: len(A).

# When len(A) == len(B), the only subsequence of B equal to A is B; so as long as A != B, the answer remains len(A).

# When A == B, any subsequence of A can be found in B and vice versa, so the answer is -1.

def findLUSlength(self, A, B):
    if A == B:
        return -1
    return max(len(A), len(B))
