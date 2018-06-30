"""
678. Valid Parenthesis String
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
"""
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool

        Apporach:
        ========
        Have two stacks, Normal stack and the Star Stack.
        1) Insert the position of "(" when we see it.. when we see ")" pop the element from the stack.
           IF empty pop the star stack.. if that is empty return false.
           insert position of "*" when we see it into the star stack
        2) at the end.. every "(" index should have a greater index in the stack for star.
           Else return false.
        """
        Count = 0
        starCount = 0
        RegStack = []
        StarStack = []
        for index,ch in enumerate(s):
            if (ch == "("):
                RegStack.append(index)
            elif (ch == ")"):
                if (len(RegStack)):
                    RegStack.pop()
                elif (len(StarStack)):
                    StarStack.pop()
                else:
                    return False
            elif (ch == "*"):
                StarStack.append(index)
        if (len(RegStack) > len(StarStack)):
            return False
        while (len(RegStack) and len(StarStack)):
            rpos = RegStack.pop()
            spos = StarStack.pop()
            if (spos < rpos):
                return False
        return True
mysol = Solution()
print (mysol.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
