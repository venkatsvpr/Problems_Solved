"""
854. K-Similar Strings
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

 

Example 1:

Input: s1 = "ab", s2 = "ba"
Output: 1
Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2
 

Constraints:

1 <= s1.length <= 20
s2.length == s1.length
s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
s2 is an anagram of s1.
"""
# Perform backtracking
# with each move.. keep track of min answer at every level
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def dfs(idx):
            # Boundary condition
            if idx == len(s1):
                return 0
            
            # since the s1 is list ,get a tuple for key
            key = tuple(s1)
            if key in d:
                return d[key]
            
            # If the chars are equal no work left
            if s1[idx] == s2[idx]:
                return dfs(idx+1)
            
            # Else try swaping out and try out the future moves.
            # Backtrack
            ans = float('inf')
            for i in range(idx+1, len(s1)):
                if s1[i] == s2[idx]:
                    # swap
                    s1[idx],s1[i] = s1[i], s1[idx]
                    ans = min(ans, 1+ dfs(idx+1))
                    # swap back
                    s1[i], s1[idx] = s1[idx],s1[i]
            # Store the answer back
            d[key] = ans
            return d[key]
        
        d = dict()
        if s1 == s2:
            return 0
        
        # get a list of s1,s2 for swapping out and trying
        s1, s2 = list(s1), list(s2)
        return dfs(0)
        