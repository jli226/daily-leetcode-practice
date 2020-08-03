# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint

# Written with love by atm1504
# Written with love by atm1504
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=0
        res=float("inf")
        t=0
        while i<n and j<n:
            t+=nums[j]
            while t-nums[i]>=s:
                t-=nums[i]
                i+=1
            if t>=s:
                res=min(res,j-i+1)
            j+=1
        if res!=float("inf"):
            return res
        return 0