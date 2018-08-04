"""
415. Add Strings
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry  = 0
        st = ""
        if len(num1)> len(num2):
            num2 = "0"*(len(num1)-len(num2))+num2
        if len(num1)< len(num2):
            num1 = "0"*(len(num2)-len(num1))+num1
        for ch1,ch2 in zip(num1[::-1],num2[::-1]):
            s = int(ch1)+int(ch2)+carry
            carry = s/10
            st += str(s%10)
        if (carry != 0):
            st += str(carry)
        return st[::-1]
