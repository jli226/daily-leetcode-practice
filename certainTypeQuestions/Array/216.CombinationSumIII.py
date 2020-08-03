# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

# Note:

# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:

# Input: k = 3, n = 9
# # Output: [[1,2,6], [1,3,5], [2,3,4]]

        answer = []
        
        for num in range(1, 10):
            self.helper(answer, [num], num, num + 1, k, n)
        
        return answer
    
    def helper(self, answer, combo, combo_sum, num, k, n):
        if combo_sum == n and len(combo) == k:
            answer.append(combo)
        elif num <= 9 and combo_sum < n and len(combo) < k:
            self.helper(answer, combo, combo_sum, num + 1, k, n)
            self.helper(answer, combo + [num], combo_sum + num, num + 1, k, n)