"""
557. Reverse Words in a String III

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

Approach:
========
Split the strings into space.
and roatate every word
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def rev (newword):
            word = list(newword)
            left = 0
            right = len(word)-1
            while (left <right):
                temp = word[left]
                word[left] = word[right]
                word[right] = temp
                left += 1
                right -= 1
            #print ("going to return ",word)
            return "".join(word)
        s = s.split(" ")
        for index,word in enumerate(s):
            s[index] = rev (str(word))
        return " ".join(s)
