"""
76. Minimum Window Substring
Hard

10060

530

Add to List

Share
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

"""
class Solution:
    def minWindow(self, s, t):
        # keep track of what we need
        need = collections.Counter(t)
        # We are missing these many characters
        missing = len(t)
        start = end = 0;
        minstart = minend  = float('-inf')
        for end,ch in enumerate(s):
            # If we come across somethig we need, reduce missing
            if (need[ch] > 0):
                missing -= 1
            need[ch] -= 1

            # We have not satisfied the condition of match. keep continuing
            if (missing > 0):
                continue
            
            # Skip Extra Characters which are from the start
            while (start<=end and need[s[start]] <0):
                need[s[start]] +=1
                start += 1
            
            # Store min-start min-end everytime.
            if (minend==float(-inf) or (end-start) <= (minend-minstart)):
                minstart,minend = start,end
        if minend == float('-inf'):
            return ""
        return s[minstart:minend+1]
        
        


def get_shortest_unique_substring(arr, str):
    def flush(level):
        print ("flush triggerd for ",level)
        count = 0
        for item in expect:
            if (expect[item] == -1):
                continue;
            if (expect[item] <= level):
                expect[item] = -1
                count += 1
        return count

    expect = dict()
    for item in arr:
      expect[item] = -1
      if (item not in str):
        return ""
    Shortest = str
    inc_count = 0
    for index,ch in enumerate(str):
        if (ch not in expect):
            continue
        if (expect[ch] == -1):
            expect[ch] = index
            inc_count += 1
        else:
            inc_count -= flush(expect[ch])
            if (inc_count < 0):
                inc_count = 0
            inc_count += 1
            expect[ch] = index
        print (expect)
        if (inc_count == len(arr)):
            print (expect)
            ma = float('-inf')
            mi = float('inf')
            for key in expect:
                mi = min (mi, expect[key])
                ma = max (ma, expect[key])
            print (mi,ma)
            if (ma-mi < len(Shortest)):
                Shortest = str[mi:ma+1]
    return Shortest
print (get_shortest_unique_substring(["x","y","z"], "xyyzyzyx"))
