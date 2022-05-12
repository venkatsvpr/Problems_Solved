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
        t = [[ -1 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        for x in range(len(text1)+1):
            for y in range(len(text2)+1):
                if x == 0 or y == 0:
                    t[x][y] = 0
    
        for numi in range(1,len(text1)+1):
            for numj in range(1,len(text2)+1):
                # Either we pick the characters and we have a subproblem
                if text1[numi-1] == text2[numj-1]:
                    t[numi][numj] = 1 + t[numi-1][numj-1]
                else:
                    # We dont pick them and there are two possible subproblems. we find the max of the two
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
        return t[len(text1)][len(text2)]