# Guess Number higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0):
            reQturn -1;  
        else:
            start = 0
            end = n
            mid = 0 
            while (start <= end):
                mid = (start + end )/ 2
                retval = guess(mid)
                print ("start",start,"end",end,"mid",mid,"retval",retval)
                if (retval<0):
                    end =mid;
                elif (retval == 0):
                    return mid
                elif (retval >0):
                    start = mid+1
               
