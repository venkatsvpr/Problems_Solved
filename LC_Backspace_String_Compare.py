"""
844. Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
"""

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        S_Stack = []
        T_Stack = []
        for char in S:
            if (char == "#"):
                if (len(S_Stack)):
                    S_Stack.pop()
            else:
                S_Stack.append(char)

        for char in T:
            if (char == "#"):
                if (len(T_Stack)):
                    T_Stack.pop()
            else:
                T_Stack.append(char)

        if ("".join(T_Stack) == "".join(S_Stack)):
            return True
        else:
            return False

mysol =Solution()
S = "ab#c"
T = "ad#c"
print (mysol.backspaceCompare(S,T))

S = "ab##"
T = "c#d#"
print (mysol.backspaceCompare(S,T))

S = "a##c"
T = "#a#c"
print (mysol.backspaceCompare(S,T))

S = "a#c"
T = "b"
print (mysol.backspaceCompare(S,T))
