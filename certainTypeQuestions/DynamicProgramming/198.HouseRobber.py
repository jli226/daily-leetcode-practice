You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1, 2, 3, 1]
Output: 4
Explanation: Rob house 1 (money=1) and then rob house 3 (money=3).
Total amount you can rob = 1 + 3 = 4.


class Solution(object):
    def rob(self, nums):
        # Base Case: nums[0] = nums[0]
        # nums[1] = max(nums[0], nums[1])
        # nums[k] = max(k + nums[k-2], nums[k-1])
        '''
        # Approach 1:- Construct dp table
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
          dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1] # return the last element
        '''

        # Approach 2:- Constant space use two variables and compute the max respectively
        prev = curr = 0
        for num in nums:
            temp = prev  # This represents the nums[i-2]th value
            prev = curr  # This represents the nums[i-1]th value
            curr = max(num + temp, prev)  # Here we just plug into the formula
        return curr
