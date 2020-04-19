# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1, 3, 5, 6], 5
# Output: 2


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
