# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:

# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        own_last = -prices[0]
        not_own_last2 = 0
        not_own_last = 0
        for i in range(1, len(prices)):
            own = max(own_last, not_own_last2 - prices[i])
            not_own = max(not_own_last, own_last + prices[i])

            not_own_last2 = not_own_last
            own_last = own
            not_own_last = not_own
            res = max(res, max(own, not_own))
        return res
