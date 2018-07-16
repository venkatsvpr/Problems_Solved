"""
516. Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

"""
"""
Simple dp solution
https://www.youtube.com/watch?v=_nCsPn7_OgI

If s[i] == s[j]
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(set(s)) == 1):
            return len(s)
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        #print (dp)
        ToVisit = []
        for i in range(len(s)):
            ToVisit.append((0,i))
        #print (ToVisit)
        while (ToVisit):
            i,j = ToVisit.pop(0)
            #print ("going for i,j",i,j)
            while ((i <len(s)) and (j <len(s))):
                if (i == j) and (s[i] == s[j]):
                    dp[i][j] = 1
                elif (s[i]==s[j]):
                    dp[i][j] = 2 + dp[i+1][j-1]
                elif (s[i] != s[j]):
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])
                i += 1
                j += 1
        #print (dp)
        return dp[0][len(s)-1]
