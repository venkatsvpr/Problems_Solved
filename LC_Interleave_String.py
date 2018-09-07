"""
97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

"""

"""
- Looks tough but simple to be solved with dp.
- set 0,0 to True.
- if (i == 0) and s2[j-1] == s3[i+j-1] then dp[i][j] = dp[i][j-1]
- if (j == 0) and s1[i-1] == s3[i+j-1] then dp[i][j] = dp[i-1][j]
else.. dp[i][j]  =  (s2[j-1] == s3[i+j-1] and dp[i][j] = dp[i][j-1]) or (s1[i-1] == s3[i+j-1] and dp[i][j] = dp[i-1][j])
answer will be at dp[len(s1)][len(s2)]
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if (len(s3) != len(s1) + len(s2)):
            return False
        dp = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(1+len(s1)):
            for j in range(1+len(s2)):
                if (i==0) and (j==0):
                    continue
                if (i == 0):
                    dp[i][j] = dp[i][j-1] and (s2[j-1] == s3[i+j-1])
                elif (j == 0):
                    dp[i][j] = dp[i-1][j] and (s1[i-1] == s3[i+j-1])
                else:
                    # set true if any of the above two cases are true
                    dp[i][j] = (dp[i][j-1] and (s2[j-1] == s3[i+j-1])) or dp[i-1][j] and (s1[i-1] == s3[i+j-1])
        return dp[len(s1)][len(s2)]
