""" Shortest Palindrome 
https://leetcode.com/problems/shortest-palindrome/description/
"""
class Solution:
    def shortestPalindrome(self, s):
        """ Find the reversed of the string """
        rev_s = s[::-1]
        
        for i in range(len(s) + 1):
            """ Check if revs[i:] is a substring of s"""
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s
