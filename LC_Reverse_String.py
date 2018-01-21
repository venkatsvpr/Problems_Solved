"""
Reverse a string
"""
class Solution(object):
    def reverseString(self, s):
        r = list(s)
        i = 0;
        j = len(r)-1;
        while (i<j):
            r[i],r[j] = r[j],r[i]
            i = i+1;
            j = j-1;
        return "".join(r)
