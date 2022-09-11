"""
1312. Minimum Insertion Steps to Make a String Palindrome

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def rec(start, end):
            # boundary condition
            if start >= end:
                return 0
            
            # check if equal
            if s[start] == s[end]:
                return rec(start+1, end-1)
            
            # not equal We can insert in right or left
            return 1 + min(rec(start+1, end), rec(start, end-1))
        return rec(0,len(s)-1)
