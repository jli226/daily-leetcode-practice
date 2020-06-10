# A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

# For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

# Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

# Example 1:

# Input: [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence.


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # trivial case
        if (len(nums) < 2):
            return len(nums)
        # create array of diffs
        diffs = []
        for i in range(1, len(nums)):
            x = nums[i] - nums[i - 1]
            # ignore diffs of 0 as they don't count as turning points
            if (x != 0):
                diffs.append(x)
        # if there were diffs of only 0, then seq length is 1
        if (not diffs):
            return 1

        cnt = 1  # min seq length at this stage
        # now count the number of times the sign of diff between consecutive numbers changes
        # that will be equal to the max wiggle subseq length
        for i in range(1, len(diffs)):
            prod = diffs[i] * diffs[i - 1]
            if (prod < 0):
                cnt += 1

        return cnt + 1
