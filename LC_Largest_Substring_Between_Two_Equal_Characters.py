"""
1624. Largest Substring Between Two Equal Characters

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
Example 4:

Input: s = "cabbac"
Output: 4
Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".
 

Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.

"""
import collections
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = collections.defaultdict(set)
        anyTwice = False
        chrs = set()
        for idx,ch in enumerate(s):
            chrs.add(ch)
            charSet[ch].add(idx)
            if len(charSet[ch]) > 1:
                anyTwice = True
        if not anyTwice:
            return -1
        maxLen = -1
        for ch in chrs:
            start = -1
            for idx in sorted(charSet[ch]):
                if (start == -1):
                    start = idx
                    continue
                maxLen = max(maxLen, idx-start-1)
        return maxLen