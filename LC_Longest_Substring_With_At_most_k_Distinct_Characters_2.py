"""
340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""
"""
Approach:
Idea is very simple..
have a modving window and keep track of the number of characters.. also see if there are 2 distint chracters.
this can be found by the number of len of the counter collection.
if the lenght is more .. then move the start to match the k

this is similar to 2 discint characters.. change 2 by k
also handle k==0 .. return 0 default case
compute the maxlenght
"""
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        """
        :type s: str
        :rtype: int
        """
        if (k == 0):
            return 0
        if (len(s) == 0):
            return 0
        c = collections.Counter()
        start  = end = 0
        maxlen = 0
        for end,ch in enumerate(s):
            c[ch] += 1
            if (len(c) < k):
                maxlen = max(maxlen,end-start)
                continue
            while (len(c) > k):
                c[s[start]] -= 1
                if (c[s[start]] == 0):
                    del c[s[start]]
                start += 1
            maxlen = max(maxlen,end-start)
        return maxlen+1
