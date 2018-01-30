"""
If there are 1 step, it can be taken in 1 way
if there are 2 steps. it cann be done in 2 ways.. (2steps or 2*1steps)
Rest can be achieveid by 1 or 2 steps.
"""
d = dict()
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in d:
            return d[n]
        if (n <= 1):
            d[n] = n
            return n
        elif (n == 2):
            d[2] = 2
            return 2
        else:
            result = self.climbStairs(n-1) + (self.climbStairs(n-2))
            d[n] = result
            return result
