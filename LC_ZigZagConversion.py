"""
Zigzag conversion
https://leetcode.com/problems/zigzag-conversion/description/
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        L = [''] * numRows
        index, step = 0, 1

        for ch in s:
            L[index] += ch
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        
        return ''.join(L)
