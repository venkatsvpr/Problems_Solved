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
            
