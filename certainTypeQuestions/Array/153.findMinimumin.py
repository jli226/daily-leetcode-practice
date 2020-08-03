# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # -------------------------------------------
        
        def helper(left, right):
            
            # base case also known as stop condition
            if (right - left) <= 1:
                return min(nums[left], nums[right])
            
            
            # general case
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # minimum is on the right half
                return helper(mid+1, right)
            
            else:
                # minimum is on the left half
                return helper(left, mid)
            
        # -------------------------------------------
        
        return helper(left=0, right=len(nums)-1)