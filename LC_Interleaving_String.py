"""
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

 

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?

"""
class Solution:
    def __init__(self):
        self.d = dict()
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def rec (x, y, z):
            d = self.d
            # Get precomputed Answer
            if (x,y,z) in d:
                return d[(x,y,z)]
            if z >= len(s3):
                if x == len(s1) and y == len(s2):
                    d[(x,y,z)] = True
                else:
                    d[(x,y,z)] = False
                return d[(x,y,z)]
            if x >= len(s1) and y >= len(s2):
                d[(x,y,z)] = False
                return d[(x,y,z)]
            # Check if s1 can be interleaved 
            if x < len(s1) and s1[x] == s3[z]:
                if True == rec(x+1,y,z+1):
                    d[(x,y,z)] = True
                    return d[(x,y,z)]
            # Check if s2 can be interleaved
            if y < len(s2) and s2[y] == s3[z]:
                if True == rec(x, y+1, z+1):
                    d[(x,y,z)] = True
                    return d[(x,y,z)]
            # Else we have to return false
            d[(x,y,z)] = False
            return d[(x,y,z)]
        # can check if the char counts and frequencies match
        return rec(0,0,0)