"""
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        Approach:
        1) Set the left=0 and right=n-1
        2) check if the s[left] == s[right] then left++, right--
        3) for the first mismatch. set a bit to denote that it is wrong.. And find the possible future moves.
        4) Try one.. if it fails try other.
        """
        mismatch = False
        left = 0
        right = len(s)-1
        ToDo = list()

        while (left < right):
            if (s[left] != s[right]):
                if (mismatch == True):
                    if (len(ToDo) > 0):
                        (left,right) = ToDo.pop()
                        continue;
                    return False
                mismatch = True
                # If the next possible move is left+1
                if (s[left+1] == s[right]):
                    ToDo.append((left+1,right))
                # If the next possible move is right-1
                if (s[right-1] == s[left]):
                    ToDo.append((left,right-1))
                if (len(ToDo)):
                    (left,right) = ToDo.pop()
            else:
                left += 1
                right -=1
        return True
  mysol = Solution()
  mysol.validPalindrome("abca")
