"""
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.


Approach:
    If two numbers of size m and n is multipled.. the max output can be m+n
    "9" * "9" = "81"
    so create an interger list of size m + n and take digit by digit of both inputs and multily and keep addding it ot thelist.
    at the end.. from the units place modulo it and take the quotient to the next digit.
    at the end convert all to string and return.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # Multiply digit by digit
        n1 = list(num1)
        n2 = list(num2)
        Ans = [0] * ((len(num1))+(len(num2)))
        for i1,c1 in enumerate(reversed(n1)):
            for i2,c2 in enumerate(reversed(n2)):
                Ans[i1+i2] += int(c1)*int(c2)

        zeroFlag = True
        carry = 0

        # Accumulation of the answer
        for i in range(len(Ans)):
            Ans[i] += carry
            carry = Ans[i]/10
            Ans[i] = Ans[i]%10
            if (Ans[i] > 0) or (carry > 0):
                zeroFlag = False
        if (zeroFlag == True):
            return "0"

        # clear the leading zeros
        if Ans[i] == 0:
            del (Ans[i])

        # Convert it to string and return
        return "".join(reversed(map(str,Ans)))
