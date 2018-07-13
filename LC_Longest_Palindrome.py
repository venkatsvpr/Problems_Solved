"""
409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""
import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = False
        Ans = odd = 0
        count = collections.Counter(s)
        for key in count:
            if (count[key]%2 == 0):
                Ans += count[key]
            else:
                odd = True
                Ans += count[key]-1
        if (odd == True):
            Ans += 1
        return Ans
