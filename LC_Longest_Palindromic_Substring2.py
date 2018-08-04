"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
Approach:
This is a o(N^2) solution.
pick all points and expand around that and see if it is a  palindrome
"""

class Solution(object):
    def longestPalindrome(self, S):
        """
        :type s: str
        :rtype: str
        """
        def expand_me(start,end,st):
            #print ( start,end,st)
            count = 0
            best_start = best_end = 0
            while (st[start] == st[end]):
                if (start == end):
                    count += 1
                else:
                    count += 2
                best_start = start
                best_end = end
                start -= 1
                end += 1
                if (start < 0) or (end >= len(st)):
                    break
            #print (" returning ",count,best_start,best_end)
            return count,best_start,best_end
        s = str(S)
        max_count = 0
        best_start = best_end = -1
        for i in range(0,len(s)):
            #print ("max beststart and end " ,max_count,best_start,best_end)
            c,st,en = expand_me(i,i,s)
            if (c > max_count):
                best_start = st
                best_end = en
                max_count = c
        for i in range(0,len(s)-1):
            #print ("max beststart and end " ,max_count,best_start,best_end)
            c,st,en = expand_me(i,i+1,s)
            if (c > max_count):
                best_start = st
                best_end = en
                max_count = c
        #print (best_start,best_end)
        return s[best_start:best_end+1]
