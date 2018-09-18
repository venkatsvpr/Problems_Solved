"""
394. Decode String

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

"""
When we see a [ or any character. push it to stack
If we see "]" pop everything till "[" and repeat the chracters seen for the number just seen before that.
push the answer back to stack and keep doing the same things.
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        Ans = ""
        stack = []
        for ch in s:
            if (ch != "]"):
                stack.append(ch)
            else:
                St = ""
                while (stack[-1] != "["):
                    St = stack.pop() + St
                stack.pop()
                Num = stack.pop()
                #print (St*int(Num),stack)
                stack.append(St*int(Num))
        return "".join(stack)

                
