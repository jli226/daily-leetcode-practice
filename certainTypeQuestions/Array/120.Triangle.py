# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:

# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # If the input is empty, the minimum sum is 0
        if not triangle:
            return 0
        
        # Get number of rows in the input
        rows = len(triangle)
        
        # If there is only one row, the minimum sum is the value of first row.
        if rows == 1:
            return triangle[0][0]
        
        # Traverse from the second last row to the first row.
        for i in range(rows - 2, -1, -1):
            
            # Then iterate through every element in this row.
            # Every element in this row = (current value) + min(left, right)
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        # At the end, the value of first row is the answer.
        return triangle[0][0]