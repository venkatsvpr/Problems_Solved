# Longest Absolute File Path
# https://leetcode.com/problems/longest-absolute-file-path/
class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lines = input.split('\n')
        longest = 0;
        level_value = [None] * len(lines)
        for line in lines:
            level = line.rfind('\t') + 1
            length = len(line)-  level + 1
            if (level > 0):
                level_value[level] = level_value[level-1] + length
            elif (level == 0):
                level_value[0]  = length 
            if ( -1 != line.find(".")):
                if (level_value[level] -1 > longest):
                    longest = level_value[level] -1
                
        return longest
