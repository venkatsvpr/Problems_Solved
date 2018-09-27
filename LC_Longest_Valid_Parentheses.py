"""
32. Longest Valid Parentheses


Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

"""
Loop through the character with index.
When we find "(" .. Append an index
If we find a ")" .. pop the Stack..  if the length of stack is zero
    means we have one extra ")". so append idx into a Stack
else, store the maxval everytime.
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        Stack = [-1]
        maxval = 0
        for idx,ch in enumerate(s):
            if (ch == "("):
                Stack.append(idx)
            else:
                Stack.pop()
                # If it is zero.. means there are extra ).. store the idx into Stack
                if (0 == len(Stack)):
                    Stack.append(idx)
                else:
                    # Maxvalue store idx-Stack[-1]
                    maxval = max(maxval,idx -int(Stack[-1]))
        return maxval                    
