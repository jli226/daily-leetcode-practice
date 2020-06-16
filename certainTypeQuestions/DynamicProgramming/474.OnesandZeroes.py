
# Example 2:

# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".


# Constraints:

# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i] consists only of digits '0' and '1'.
# 1 <= m, n <= 100
# Accepted
# 46,539
# Submissions
# 109,599
# Contributor
# piy9

# Problems

# Pick One

# Prev
# 474/1483

# Next

# Autocomplete

class Solution(object):
    def findMaxForm(self, strs, m, n):

        dp = [[0] * (n+1) for _ in range(m+1)]

        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')

        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])

        return dp[m][n]
