"""
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        d = {}
        def lcs(idx1, idx2):
            if (idx1,idx2) in d:
                return d[(idx1, idx2)]
            
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            
            # We have two decisions, pick the number or not pick the number
            # Pick it
            if text1[idx1] == text2[idx2]:
                d[(idx1, idx2)] = 1 + lcs(idx1+1, idx2+1)
                return d[(idx1, idx2)]
            
            # Not pick it
            d[(idx1, idx2)] = max(lcs (idx1+1, idx2 ) ,lcs (idx1, idx2+1))
            return d[(idx1, idx2)]
        return lcs(0,0)