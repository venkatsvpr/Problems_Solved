"""
201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

when there are two numbers.. m and n.. try to find the common portion..
for example.
we try to find the range 9 to 15.
1001 to 1111.
but in the middle ther will be numbers like 1100..
So we have to find the common part..so keep rightshfting both numbers till they are equal.
when they are equal again left shift to count times.. and that will be our answer.
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = 0
        while (m != n):
            n = n >> 1
            m = m >> 1
            count += 1
        return n<<count
