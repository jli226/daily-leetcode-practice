# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:

# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:

# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        for i in range(len(nums)): 
            if i == 0 or nums[i-1] + 1 != nums[i]: stack = [nums[i]]
            if i == len(nums)-1 or nums[i] + 1 != nums[i+1]: 
                if stack[-1] != nums[i]: stack.append(nums[i])
                ans.append(stack)
        return ["->".join(map(str, x)) for x in ans]