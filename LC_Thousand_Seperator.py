"""
1556. Thousand Separator

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
Example 3:

Input: n = 123456789
Output: "123.456.789"
Example 4:

Input: n = 0
Output: "0"
 

Constraints:

0 <= n < 2^31
"""
class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        stack = list()
        while (n):
            stack = [ n%10 ] + stack
            n /= 10
        if (len(stack) == 0) :
            return "0"
        ans = ""
        count = 0
        while(len(stack)):
            if (count == 3):
                ans  = "."+ans
                count = 0
            ans = str(stack.pop()) + ans
            count += 1
        return ans