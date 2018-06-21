"""
202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Approach: Use hash to store the square of number from 0 to 9 and also the seen numbers.

"""
"""
"""
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        Seen = dict()
        Square = dict()
        for i in range(10):
            Square[i]  = i*i
        while (n not in Seen):
            if(n == 1):
                return True
            Seen[n] =True
            temp = n
            sq  = 0
            while (temp):
                sq += Square[temp%10]
                temp = int (temp/10)
            n = sq
        return False

mysol = Solution()
print (mysol.isHappy(19))
