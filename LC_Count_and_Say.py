"""
38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.


Approach:
Staright forward. use string to store the result of every iteration
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(n-1):
            count = 0
            prev = s[0]
            temp = ""
            for ch in s:
                if (prev == ch):
                    count += 1
                else:
                    temp += str(count)+str(prev)
                    prev = ch
                    count = 1
            temp += str(count)+str(prev)
            s =temp
        return s

mysol = Solution()
print (mysol.countAndSay(10))
print (mysol.countAndSay(2))
