"""
856. Score of Parentheses

Given a balanced parentheses string S, compute the score of the string based on the following rule:

    () has score 1
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.



Example 1:

Input: "()"
Output: 1

Example 2:

Input: "(())"
Output: 2

Example 3:

Input: "()()"
Output: 2

Example 4:

Input: "(()(()))"
Output: 6



Note:

    S is a balanced parentheses string, containing only ( and ).
    2 <= S.length <= 50

Approach:
=========
1) If its a "(", push it to Stack
2) If its a ")" and the last element in stack is "(", pop it out and push 1 in the Stack
 If its a ")" and the last element is not "(" add all the elements till "(" and multiply it by two.
 pop out "(" and insert the number back
At the end return the sum of the elements in the stack
"""
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        temp = 0
        St = []
        Num = [0]
        s = 0
        for ch in S:
            if (ch == "("):
                St.append(ch)
            else:
                if (St[-1] == "("):
                    St.pop()
                    St.append(1)
                else:
                    out = St.pop()
                    if (St[-1] == "("):
                        St.pop()
                        St.append(2*out)
                        continue;
                    else:
                        s = out
                        while (St[-1] != "("):
                            s += St[-1]
                            St.pop()
                        St.pop()
                        St.append(2*s)
        return sum(St)
