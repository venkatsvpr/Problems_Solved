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

"""
When a price is less than previous day price.. consider todays price as the buy price.
if todays price is greater than previous day price... then sell it today and buy it again today.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        res = 0;
        buy_price = -1;
        for index,item in enumerate(prices):
            if (buy_price == -1):
                buy_price = item
                continue;
            if (buy_price < item):
                res += abs(item-buy_price)
                buy_price = item
                continue;
            if (buy_price > item):
                buy_price = item;
                continue;
        
        return (res)
            
