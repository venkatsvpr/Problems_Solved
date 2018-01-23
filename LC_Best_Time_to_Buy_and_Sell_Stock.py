"""
run through the numbers.. store the min_number and max_profit.
update the max_profit in the process. 
What remains at the end is the max_profit.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        for index,item in enumerate(prices):
            if (item < min_price):
                min_price = item
            if ((prices[index]-min_price) > max_profit):
                max_profit = prices[index] - min_price;
        return (max_profit)
