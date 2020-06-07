# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

# Example 1:

# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:

# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        list_3 = [3] * (n/3)  # generate a list of 3
        mod_3 = n % 3
        if mod_3 == 1:  # if a 1 is left, then add it to the first element to get a 4
            list_3[0] += 1
        if mod_3 == 2:  # if a 2 is left, then put it into the list
            list_3.append(2)
        return reduce(lambda a, b: a*b, list_3)
