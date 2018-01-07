"""
Isomorphic String
Find len(s) == len(t) == len(set(zip(s,t)))
If this is true. Return True else Return False
"""
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if ((len(s) ==0) and (len(t)==0)):
            return True;
        if (len(set(s)) != len(set(t))):
            return False;
        if (len(set(s)) != len(set(zip(s,t)))):
            return False;
        return True
