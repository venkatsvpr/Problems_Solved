"""
340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

#   For example, Given s = eceba and k = 2,

#T is ece which its length is 3.

Approach:
========
The problem is fairly straight forward
have a window and keep adding characters to the window till the number of unique charaters is less than k
if it is greater.. remove chracters from the left
find the max len at every step
"""
import collections
def longestSubstring ( s, k):
    c  = collections.Counter()
    for ch in s:
        c [ch] += 1
    if (k > len(c)):
        return None
    if (k == len(c)):
        return s
    left = 0
    right = 0
    maxlen = 0
    maxl = 0
    maxr = 0
    sub_str = collections.Counter()
    while (right < len(s)):
        if (len(sub_str) == 0):
            sub_str[s[right]] += 1
            if ((right - left +1 ) > maxlen):
                maxr = right
                maxl = left
                maxlen = right -left + 1
            right += 1
            continue;
        sub_str[s[right]] += 1
        right += 1
        while (len(sub_str) > k):
            sub_str[s[left]] -= 1
            if (sub_str[s[left]] == 0):
                del (sub_str[s[left]])
            left += 1
        if (right -left + 1)  > maxlen:
            maxr = right
            maxl = left
            maxlen = right - left + 1
    if (right -left + 1) > maxlen:
        maxr = right
        maxl = left
        maxlen = right - left + 1
    print (s[maxl:maxr])
longestSubstring ("eeewceeeeeeeeeeeeba",2)
