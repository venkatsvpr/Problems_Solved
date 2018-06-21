"""
258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

"""

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int

        Approach: abc can be seen as 100a + 10b + c
        (num) % 9
        => (100a + 10b + c)%9
        => (99a + a + 9b + b + c) %9
        => (a + b + c)%9
        Since we are repeatedly summing the result can be between 0 to 9.
        If the num is zero we return  0.
        If we return 9 if the num%9 is zero.
        else we return whatever value num%9 is
        """
        if (num == 0):
            return 0
        if (num % 9 == 0):
            return 9
        return num%9
