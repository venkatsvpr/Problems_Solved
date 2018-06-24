"""
859. Buddy Strings
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
Example 1:

Input: A = "ab", B = "ba"
Output: true

Example 2:

Input: A = "ab", B = "ab"
Output: false

Example 3:

Input: A = "aa", B = "aa"
Output: true

Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

Example 5:

Input: A = "", B = "aa"
Output: false
Note:

    0 <= A.length <= 20000
    0 <= B.length <= 20000
    A and B consist only of lowercase letters.

Approach:
==========
1) If there is a difference of set of the two strings..return false
2) if there are only two different places.. return True
3) if there are exactly same.. check if there are duplicate charactes.. return True
return false other wise.
"""

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        count = 0
        if (set(A) != set(B)):
            return False
        for ch1,ch2 in zip(A,B):
            if (ch1 != ch2):
                count += 1
        if (count == 2):
            return True
        if (count == 0):
            if (len(set(list(A))) < len(A)):
                return True
        return False
