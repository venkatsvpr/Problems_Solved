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
This is a nice logic.
First insert ["",1] into the stack.
When we see a num.. keep track of the num
when we see a [, insert ["", int(num)] into the stack
then whtaver character we see.. add it inot that element.. stack[-1][0] +=ch
when we see a ], pop the element out.. and repeat it by the size and store it in the last element on stack.
keep doing it..
ultimately the answer will be there on the first element of the stack.

"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        Stack = []
        Stack.append(["",1])
        Num = ""
        for ch in s:
            print (ch,Stack)
            if (ch.isdigit()):
                Num += ch
            elif (ch == "["):
                Stack.append(["",int(Num)])
                Num = ""
            elif (ch == "]"):
                St,size = Stack.pop()
                Stack[-1][0] += St*size
            else:
                Stack[-1][0] += ch
        return Stack[0][0]
 
