"""
Loop through the bigger string and maintain the number of times one character is seen
Loop thorugh the smaller string and decrememnt the character
Whatever is remaining is not present in the smaller string. That is the answer
"""
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        Big = ""
        Small = ""
        if (not s and not t):
            return ""
        
        if (not s):
            if (len(t) == 1):
                return t[0]
            else:
                return ""
            
        if (len(s)>len(t)):
            Big = s
            Small = t
        else:
            Big = t
            Small = s
        
        for char in Big:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        for char in Small:
            if char not in d:
                return char
            else:
                d[char] -= 1
        
        for char in d:
            if (d[char] == 1):
                return char
