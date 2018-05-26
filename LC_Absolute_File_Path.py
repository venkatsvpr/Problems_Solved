# Longest Absolute File Path
# https://leetcode.com/problems/longest-absolute-file-path/
class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # Split the input based on new line
        lines = input.split('\n')
        longest = 0;
        # Create an array of None. This will be used to store the lenght for each level.
        level_value = [None] * len(lines)
        for line in lines:
            # find the position of the last tab space.
            level = line.rfind('\t') + 1
            # find the length of the text
            length = len(line)-  level + 1
            if (level > 0):
                # add the lenght till the previous level to the lenght nd store it back in the level
                level_value[level] = level_value[level-1] + length
            elif (level == 0):
                # store the length of the level in the array
                level_value[0]  = length
            if ( -1 != line.find(".")):
                # When we find the file (found by the dot) take the level value and do a -1 for the last / added.
                # Compare it with the longest value and store it.
                if (level_value[level] -1 > longest):
                    longest = level_value[level] -1
                
        return longest
