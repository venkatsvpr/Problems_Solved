""" 859. Buddy Strings
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
 

Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.

"""


class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        ## The lengths are not equal then we cannot swap and reach the answer
        if len(s) != len(goal):
            return False
        
        ## If both are same, if there are some duplicates we can swap and still make the answer
        if s == goal and len(set(s)) < len(goal):
            return True
        
        ## Track all the differences, We need exactly two differences and they have to be [a,b][b,a]
        diff = [(a,b) for a,b in zip(s,goal) if a != b]
        if len(diff) == 2 and diff[0] == diff[1][::-1]:
            return True
        
        ## WE cannot make it otherwise
        return False