"""
186. Reverse Words in a String II


Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""

"""
Approach:
Reverse the whole list.
Reverse words by individual words again
"""
class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(start, end, lt):
            if (start == None):
                return
            while (start < end):
                str[start], str[end] = str[end], str[start]
                start += 1
                end -= 1
        # Reverse  the whole list
        reverse (0, len(str)-1, str)
        start = None
        for i in range(len(str)):
            if (str[i] == " "):
                reverse(start, i-1, str)
                start = None
            elif (start == None):
                start = i
        reverse(start,len(str)-1, str)
                
