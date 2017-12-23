# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s)== 0):
            return -1
        lt = []
        d = dict()
        for index,c in enumerate(s):
            if c not in d:
                d[c] = index
                lt.append(c)
            else:
                if c in lt:
                    lt.remove(c)
                
        if (len(lt) == 0):
            return -1
        return (d[lt[0]])
