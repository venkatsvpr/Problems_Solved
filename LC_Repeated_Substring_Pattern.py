"""
459. Repeated Substring Pattern


Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
Approach:
Start from the middle.. create a substring... of the [start:mid].. if the lenght is perfectely dividng
the input string.. repeat it and see if there is match.. else reduce the last character by one.. this will push the mid down..
ultimately we will check for single character and then break.
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        end = l-1
        start = 0
        while (start < end):
            mid = (end+1+start)/2
            tocheck = s[start:mid]
            if (tocheck*(len(s)/len(tocheck)) == s):
                return True
            end -= 1
        return False
