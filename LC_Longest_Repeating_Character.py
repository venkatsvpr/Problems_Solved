"""

424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
import collections
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def CalculateSwaps(c):
            if len(c) == 1:
                return 0
            maxKey = 0
            maxVal = 0
            for k in c:
                if maxVal == 0:
                    maxVal = c[k]
                    maxKey = k
                    continue
                if c[k] > maxVal:
                    maxVal = c[k]
                    maxKey = k
            Swaps = 0
            for k in c:
                if (k != maxKey):
                    Swaps += c[k]
            return Swaps
        c = collections.Counter()
        i = 0 
        Ans = 0
        for j,ch in enumerate(s):
            c[ch] += 1
            swaps = CalculateSwaps(c)
            if k >= swaps:
                Ans = max(Ans, j-i+1)
            else:
                c[s[i]] -= 1
                i += 1
        return Ans

import collections
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = maxfreq = 0 
        c = collections.Counter()
        for r in range(len(s)):
            c[s[r]] += 1
            # We track the max freq which will help us an answer of atleast (maxfreq + k)
            # While keeping the door open to increasing maxfreq
            maxfreq = max(maxfreq, c[s[r]])
            if r -l + 1 > maxfreq + k:
                c[s[l]] -= 1
                l += 1
        return len(s) - l
            