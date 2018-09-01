"""
125. Valid Palindrome


Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        s = s.lower()
        while (left <right):
            if (not s[left].isalnum()):
                left += 1
                continue;
            if (not s[right].isalnum()):
                right -= 1
                continue;
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
            continue
        return True
