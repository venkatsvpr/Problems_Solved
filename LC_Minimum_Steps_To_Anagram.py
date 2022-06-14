"""
1347. Minimum Number of Steps to Make Two Strings Anagram

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
 

Constraints:

1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.

"""

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = collections.Counter()
        for ch in s:
            count_s[ch] += 1
        count_t = collections.Counter()
        for ch in t:
            count_t[ch] += 1
        replacements = 0
        for ch in range(ord('a'), ord('z')+1):
            replacements += abs(count_s[chr(ch)] - count_t[chr(ch)])
        return int(replacements/2)