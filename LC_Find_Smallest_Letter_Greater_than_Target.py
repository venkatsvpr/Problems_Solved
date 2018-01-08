"""
Do ord and find the minimum and return the letter
"""
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ord_target = ord(target)
        for letter in letters:
            ord_letter = ord(letter)
            if (ord_target < ord_letter):
                return letter;
        return letters[0]   
