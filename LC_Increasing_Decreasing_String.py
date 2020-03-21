"""
1370. Increasing Decreasing String

	Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

 

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
Example 3:

Input: s = "leetcode"
Output: "cdelotee"
Example 4:

Input: s = "ggggggg"
Output: "ggggggg"
Example 5:

Input: s = "spo"
Output: "ops"
 

Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.

Logic:
We count the number of characters in the input
Loop from start to end and keep doing it..  We would be going from a to z
"""
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = dict()
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        s = ""
        forward = 1
        key = 97
        while(True):
            if (len(d) == 0):
                break;
            if (chr(key) in d):
                d[chr(key)] -= 1
                if (d[chr(key)] == 0):
                    del(d[chr(key)])
                s += chr(key)
            if (forward == 1):
                key += 1
            elif (forward == 0):
                key -= 1
            if (key > ord("z")):
                forward = 0
            elif (key < ord ("a")):
                forward = 1
        return s
