# Word Break
# https://leetcode.com/problems/word-break/description/
class Solution(object):
    def wordBreak(self, s, words):
        ok = [True]
        """
        The initial condition is assumed to be True. so we se the 0 index bit as True.
        Then we run a loop and find if we have substrings that are True.
        Incase they are true we append True to the ok list.
        When we are done with our work the last index on the ok list will be our result.
        """
        for i in range(1,len(s)+1):
            if (any(ok[j] and s[j:i] in words for j in range(i))):
                ok.append(True)
            else:
                ok.append(False)
        return ok[-1]
