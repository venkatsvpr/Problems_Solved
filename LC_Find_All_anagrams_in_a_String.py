"""
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

"""
Approach:
Have  a sliding window
1) building a counter for the expected characters
2) if we see any expected characters.. bring expected count by one. then pull expected characters by 1
3) there are ny extra chracters... move it from the start
4) if expected is zero add it to answer.
5) simple sliding window logic
"""
import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        countp = collections.Counter(p)
        expected = len(p)
        start = 0
        Ans = []
        for end,ch in enumerate(s):
            # If we expect this character reduce expected by 1
            if (countp[ch] > 0):
                expected -= 1

            # Also reduce the count of character
            countp[ch] -= 1

            # If we have extra characters. take it out
            while (countp[ch] < 0):
                if (countp[s[start]] >= 0):
                    expected += 1
                countp[s[start]] += 1
                start += 1

            # If there is no extra characters then add the start to answer
            if (expected == 0):
                Ans.append(start)
        return Ans
                
