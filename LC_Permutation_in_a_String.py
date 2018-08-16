"""
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

Approach:
=========
Have a sliding window and build the hash and then check it with the expected string hash
the loop will be in order of O(L1+L2+26check) = O(l1+l2)
"""
import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def isequal(s1map,s2map):
            for key in s1map:
                if (s1map[key] != s2map[key]):
                    return False
            return True

        if (len(s1) > len(s2)):
            return False

        l = 0
        r = len(s1)-1

        s1map = collections.Counter()
        s2map = collections.Counter()

        for i in range(len(s1)):
            s1map[s1[i]] += 1

        for i in range(len(s1)):
            s2map[s2[i]]  += 1

        while (r < len(s2)):
            #print (l,r,s1map,s2map)
            if (isequal(s1map,s2map)):
                return True
            s2map[s2[l]] -= 1
            l+= 1
            r+= 1
            if (r <len(s2)):
                s2map[s2[r]] += 1
        return False
