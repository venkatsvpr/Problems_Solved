"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

"""
Approach:
For any value x, lets assume that we are given with coins with value c1 ,c2, c3
we could use whichever is less of the following
numcoins[value] = min ((1 coin of c1)+numcoins(value-c1)) or (1 coin of c2)+numcoins(value-c2)  or (1 coin of c3)+numcoins(value-c3)
to summaries = 1 + min(numcoins[x-c1] + numcoins[x-c2] + numcoins[x-c3])

if there are n coins
it is
numcoins[value] =  1+ min (numcoins[x-c1], numcoins[x-c2],.......,numcoins[x-cn])
the breaking conditions are
numcoins[c1] = 1
numcoins[c2] = 1
...
numcoins[cn] = 1
a value of something less thna or equal to -1 will be float('inf') -> to depict imposibility

"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def rec (value, coins, f):
            if (value <= -1):
                return float('inf')
            if (value in f):
                return f[value]
            NxtLevel = [rec(value-coin, coins, f) for coin in coins if value-coin >= 0]
            if (len(NxtLevel) == 0):
                return float('inf')
            f[value] = min(NxtLevel)+1
            return f[value]
        f= dict()
        f[0] = 0
        for coin in coins:
            f[coin] = 1
        retval = rec (amount, coins, f)
        if (retval == float('inf')):
            return -1
        return retval
