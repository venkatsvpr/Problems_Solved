"""
821. Shortest Distance to a Character
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

Approach:
========
Keep a count of the character C seen in s
with this find the mininum of the character location and return answer.
"""
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        present_items = []
        for i,ch in enumerate(S):
            if (ch == C):
                present_items.append(i)


        Answer = []
        for i,ch in enumerate(S):
            min_val = float('inf')
            for val in present_items:
                min_val = min(min_val, abs(i-val))
            Answer.append(min_val)
        return (Answer)

mysol = Solution()
print (mysol.shortestToChar("loveleetcode","e"))
