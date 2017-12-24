# Word Break
# https://leetcode.com/problems/word-break/description/
class Solution(object):
    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1,len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]
