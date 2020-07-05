# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

def canJump(self, nums):
    max_reach, n = 0, len(nums)
    for i, x in enumerate(nums):
        if max_reach < i:
            return False
        if max_reach >= n - 1:
            return True
        max_reach = max(max_reach, i + x)
