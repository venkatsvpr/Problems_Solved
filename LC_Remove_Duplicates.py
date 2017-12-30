""" 
Remove Duplicates
https://leetcode.com/problems/remove-duplicate-letters/description/
"""
class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        """ """
        """ 
        1) Create the set of S (unique characs)
        2) Sort the set
        3) Take the character from the sorted set, one by one
        4) Go to the position in the string and the remaining string should contain the same characters as in the set
        5) If it contains , remove the character and recall the same function. 
        6) This will recursively make the string in lexicographical order
        
        """
        if s:
            for ch in sorted(set(s)):
                rest = s[s.index(ch):]
                if (set(rest) == set(s)):
                    return ch + self.removeDuplicateLetters(rest.replace(ch,''))
        return ''
