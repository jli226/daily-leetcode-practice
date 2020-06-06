# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:

# Input: 2
# Output: [0,1,1]
# Example 2:

# Input: 5
# Output: [0,1,1,2,1,2]


def countBits(self, num):
    """
    :type num: int
    :rtype: List[int]
    """

    iniArr = [0]
    if num > 0:
        amountToAdd = 1
        while len(iniArr) < num + 1:
            iniArr.extend([x+1 for x in iniArr])

    return iniArr[0:num+1]
