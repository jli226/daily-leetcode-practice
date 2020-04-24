# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.


# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])


class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)


class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]
