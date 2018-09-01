"""
28. Implement strStr()


Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def buildkmp (needle, kmp):
            i = 0
            j = 1
            while (j < len(needle)):
                if (needle[j] == needle[i]):
                    kmp[j] = i+1
                    j += 1
                    i += 1
                else:
                    if (i == 0):
                        j+= 1
                    else:
                        i = kmp[i-1]
            return

        kmp = [0 for i in range(len(needle))]
        buildkmp(needle,kmp)
        idx = 0
        nid  = hid = 0
        while (hid < len(haystack)):
            if (nid == len(needle)):
                return hid-len(needle)
            if (needle[nid] == haystack[hid]):
                nid += 1
                hid += 1
            else:
                if (nid == 0):
                    hid += 1
                else:
                    nid = kmp[nid-1]
        if (nid == len(needle)):
            return hid-len(needle)
        return -1

            
