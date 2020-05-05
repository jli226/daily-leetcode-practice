# # 69. Sqrt(x)
# # Easy

# # 1169

# # 1779

# # Add to List

# # Share
# # Implement int sqrt(int x).

# # Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# # Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# # Example 1:

# # Input: 4
# # Output: 2
# # Example 2:

# # Input: 8
# # Output: 2
# # Explanation: The square root of 8 is 2.82842..., and since
#             the decimal part is truncated, 2 is returned.


def mySqrt(self, x):
        lo, hi = 0, x

        while lo <= hi:
            mid = (lo + hi) // 2

            if mid * mid > x:
                hi = mid - 1
            elif mid * mid < x:
                lo = mid + 1
            else:
                return mid

        # When there is no perfect square, hi is the the value on the left
        # of where it would have been (rounding down). If we were rounding up,
        # we would return lo
        return hi
