# 367. Valid Perfect Square
# Easy

# 657

# 143

# Add to List

# Share
# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false


def BinarySearch(self, num):
        left = 0
        right = num

        while left <= right:
            mid = left + (right-left)//2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False
