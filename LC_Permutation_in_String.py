"""
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False

        s1Map = collections.Counter()
        s2Map = collections.Counter()
        for idx in range(len(s1)):
            s1Map[s1[idx]] += 1
            s2Map[s2[idx]] += 1
        
        # Keep track of the matches so that we can avoid checking the whole map every time.
        matches = 0
        
        # build up the matches once
        for i in range(ord('a'),ord('z')+1):
            matches += (1 if s1Map[chr(i)] == s2Map[chr(i)] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if  matches == 26:
                return True
            
            # right character
            ch = s2[r]
            
            # Add it to s2map and update the matches
            s2Map[ch] += 1
            
            # Track the s1 == s2 on that place or s2 becoming bigger, s2 small is already tracked.
            if s1Map[ch] == s2Map[ch]:
                matches += 1
            elif s1Map[ch]+1 == s2Map[ch]:
                matches -= 1
            
            # left character
            ch = s2[l]
            
            # Remove it from s2map and update the matches
            s2Map[ch] -= 1
            
            # Track s1 == s2, or s2 just becoming less than s2
            if s1Map[ch] == s2Map[ch]:
                matches += 1
            elif s1Map[ch]-1 == s2Map[ch]:
                matches -= 1
            l += 1
        return matches == 26