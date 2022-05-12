"""
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.

"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def rec(idx1, idx2, d):
            if idx2 < 0:
                if s[idx1] == s[idx1+1]:
                    return rec(idx1-1, idx2-1) + rec(idx1-1, idx2)
                return 1
            if idx1 < 0:
                return 0
            if s[idx1] != t[idx2]:
                return rec(idx1-1, idx2)
            else:
                return rec(idx1-1, idx2-1) + rec(idx1-1, idx2)
        return rec(len(s)-1, len(t)-1)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def rec(idx1, idx2, d):
            if (idx1,idx2) in d:
                return d[(idx1, idx2)]
            if idx2 < 0:
                return 1
            elif idx1 < 0:
                return 0
            # If the string doest match delete and solve subproblem
            elif s[idx1] != t[idx2]:
                d[(idx1, idx2)]=  rec(idx1-1, idx2, d)
            # If string matches, we can pick or not. since we are looking for distinct ways add both
            else:
                d[(idx1, idx2)] = rec(idx1-1, idx2-1, d) + rec(idx1-1, idx2, d)
            return d[(idx1, idx2)]
        d = dict()
        return rec(len(s)-1, len(t)-1, d)