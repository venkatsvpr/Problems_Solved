"""
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

"""
Approach:
Create a mapping between a pattern and a string..
This mapping should persist both ways all the time.
else false.
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ptSplit = list(pattern)
        stSplit = str.split(" ")
        #print (ptSplit,stSplit)
        if (len(ptSplit) != len(stSplit)):
            return False
        hashMap = dict()
        revHash = dict()
        for pt,st in zip(ptSplit,stSplit):
            if (pt not in hashMap) and (st not in revHash):
                hashMap[pt] = st
                revHash[st] = pt
            elif (pt in hashMap) and (st in revHash):
                if (st != hashMap[pt])  or (pt != revHash[st]):
                    return False
            else:
                return False
        return True
