"""
10. Regular Expression Matching

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def rec(idx1, idx2):
            if (idx1 >= len(s) or idx2 >= len(p)):
                if (idx1 < len(s)):
                    return False
                if (idx2 < len(p)):
                    # Check for a .* or a*
                    if (idx2+1 < len(p) and p[idx2+1] == "*"):
                        return rec(idx1, idx2+2)
                    return False
                return True
            ## Handle char* and .*
            if idx2+1 < len(p) and p[idx2+1] == "*":
                if s[idx1] == p[idx2] or p[idx2] == ".":
                    return rec(idx1+1, idx2) + rec(idx1, idx2+2)
                else:
                    return rec(idx1, idx2+2)
            ## Handle .
            if p[idx2] == ".":
                return rec(idx1+1, idx2+1)
            elif s[idx1] == p[idx2]:
                return rec(idx1+1, idx2+1)
            else:
                return False
        return rec(0,0)

class Solution:
    def __init__(self):
        self.d = dict()
    def isMatch(self, s: str, p: str) -> bool:
        def rec(idx1, idx2):
            k = (idx1,idx2)
            if k in self.d:
                return self.d[k]
            
            # Handle boundary cond
            if (idx1 >= len(s) or idx2 >= len(p)):
                # Handle the rx exhausted scenario
                if (idx1 < len(s)):
                    self.d[k] = False
                    return self.d[k]
                # Handle the input exhausted but regex still there
                if (idx2 < len(p)):
                    # Check for a .* or a*
                    if (idx2+1 < len(p) and p[idx2+1] == "*"):
                        self.d[k]= rec(idx1, idx2+2)
                        return self.d[k]        
                    else: 
                        self.d[k] = False
                        return self.d[k]
                self.d[k] = True
                return self.d[k]
            
            ## Handle char* and .*
            if idx2+1 < len(p) and p[idx2+1] == "*":
                if s[idx1] == p[idx2] or p[idx2] == ".":
                    self.d[k] = rec(idx1+1, idx2) or rec(idx1, idx2+2)
                else:
                    self.d[k] = rec(idx1, idx2+2)
            ## Handle .
            elif p[idx2] == ".":
                self.d[k] = rec(idx1+1, idx2+1)
            ## Handle match
            elif s[idx1] == p[idx2]:
                self.d[k] = rec(idx1+1, idx2+1)
            ## Handle no-match
            else:
                self.d[k] = False
            return self.d[k]
        return rec(0,0)