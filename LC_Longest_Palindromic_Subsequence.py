"""
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ps = s[::-1]
        t = [[ -1 for i in range(len(s)+1)] for j in range(len(s)+1)]
        for x in range(len(s)+1):
            for y in range(len(ps)+1):
                if x == 0 or y == 0:
                    t[x][y] = 0
    
        for numi in range(1,len(s)+1):
            for numj in range(1,len(ps)+1):
                if s[numi-1] == ps[numj-1]:
                    t[numi][numj] = 1 + t[numi-1][numj-1]
                else:
                    t[numi][numj] = max(t[numi-1][numj] , t[numi][numj-1])
        """
        Ans = ""
        (x,y) = len(s),len(ps)
        while (x>0 and y>0):
            if s[x-1] == ps[y-1]:
                Ans += s[x-1]
                x= x-1
                y= y-1
            else:
                if t[x-1][y] > t[x][y-1]:
                    x = x-1
                    y = y
                else:
                    x = x
                    y = y-1
        """
        return t[len(s)][len(ps)]
        