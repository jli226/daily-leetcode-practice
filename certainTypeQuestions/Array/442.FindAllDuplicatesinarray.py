# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1: return []
        ans = []
        max_num = len(nums)+1
        
        for idx, num in enumerate(nums):
            actual_num = num % max_num
            nums[actual_num-1] += max_num
        
        for idx, num in enumerate(nums):
            if num//max_num == 2:
                ans.append(idx+1)
        
        return ans