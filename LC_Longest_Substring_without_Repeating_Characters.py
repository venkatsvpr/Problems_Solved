"""
3. Longest Substring Without Repeating Characters


Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
## Sliding window logic
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        Ans = 0
        d = dict()
        for idx,ch in enumerate(s):
            if ch in d:
                i = max(i, d[ch])
            Ans = max(Ans , (j-i)+1)
            d[ch] = idx+1
            j+= 1
        return Ans
            