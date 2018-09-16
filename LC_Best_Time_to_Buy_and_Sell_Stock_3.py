"""
123. Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

"""
This is a logically a simple one.
At any point of time there are two decisions can be made.. buy or sell.. this has to be made twice
so 4 decisions.
we either buy or dont buy. we either sell or dont sell
We buy second time or dont buy. we either sell again or dnt seell

do in the order 2 then 1.. because we need preivious 1st decision for making this 2nd decision.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        for price in prices:
            sell2 = max(sell2, buy2+price)
            buy2 = max(buy2, sell1-price)
            sell1 = max(sell1, buy1+price)
            buy1 = max(buy1, -price)
        return sell2
