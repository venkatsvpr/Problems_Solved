"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if (n == 1):
            if s[0] > "0":
                return 1
            else:
                return 0
        if (s[0] == "0"):
            return 0
        # Store the counts
        count = [0] *(n+1)
        count[0] = 1
        count[1] = 1
        # If i-1 is greater than zero then set the count[i] to count[i-1]
        # If i-2 is 1 .. or i-2 is 2 and i-1 <7 add count[i-2] to count[i]
        for  i in range(2,n+1):
            count[i] = 0
            if (str(s[i-1]) > "0"):
                count[i] = count[i-1]
            if (s[i-2] == '1') or ((s[i-2] == '2') and (s[i-1] < '7')):
                count[i] += count[i-2]
        # count[n] will be the answer.
        return count[n]
