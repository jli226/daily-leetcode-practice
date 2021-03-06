# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

# Example:

# nums = [1, 2, 3]
# target = 4

# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)

# Note that different sequences are counted as different combinations.

# Therefore the output is 7.


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (1+target)
        for num in nums:
            if num <= target:
                dp[num] = 1
        for i in range(target+1):
            for num in nums:
                if i - num > 0:
                    dp[i] += dp[i-num]
        return dp[-1]
