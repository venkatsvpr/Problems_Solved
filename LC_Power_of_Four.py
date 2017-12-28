# Power of 4
# https://leetcode.com/problems/power-of-four/description/ 
import math
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num <= 0):
            return False
        
        rem = math.log10(num)/math.log10(4)
        if (rem == int(rem)):
            return True
        
        return False
