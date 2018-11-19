"""
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""

"""
Just check the values 
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        def isCap(ch):
            if ("A" <= ch <= "Z"):
                return True
            return False

        if (all([not isCap(ch) for ch in word])):
            return True
        if (all([isCap(ch) for ch in word])):
            return True
        Lt = []

        for ch in word:
            if (isCap(ch)):
                Lt.append(1)
            else:
                Lt.append(0)

        ans = sum(Lt)
        if (ans > 1):
            return False
        if (ans == 1) and isCap(word[0]):
            return True
        return False