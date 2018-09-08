"""
159. Longest Substring with At Most Two Distinct Characters

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""

"""
Approach:
Idea is very simple..
have a modving window and keep track of the number of characters.. also see if there are 2 distint chracters.
this can be found by the number of len of the counter collection.
if the lenght is more .. then move the start to match the 2
compute the maxlenght
"""
import collections
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0):
            return 0
        c = collections.Counter()
        start  = end = 0
        maxlen = 0
        for end,ch in enumerate(s):
            c[ch] += 1
            if (len(c) < 2):
                maxlen = max(maxlen,end-start)
                continue
            while (len(c) > 2):
                c[s[start]] -= 1
                if (c[s[start]] == 0):
                    del c[s[start]]
                start += 1
            print (start,end)
            maxlen = max(maxlen,end-start)
        return maxlen+1

            
