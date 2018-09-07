"""
524. Longest Word in Dictionary through Deleting



Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""

"""
Approch.

Write a cmp funciton to prioritize the length and then the lexicographic order.
use this and sort the input.
After this pick word one by one and see if ourstring can be deleted or chagned to get the word
simply we have to check if that word from dictionary can be obtained for deletting chracters from the input.. we have to preserve the order
so dont use counter.. rather use a 0(m+n) search to find if the word exists in the string
"""
import functools
class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def cmp (s1,s2):
            if (len(s1) > len(s2)):
                return -1
            if (len(s2) > len(s1)):
                return 1
            if (s2 > s1):
                return -1
            else:
                return 1

        def compfunc (haystack, needle):
            n_ptr = 0
            h_ptr = 0
            while ((n_ptr < len(needle)) and (h_ptr < len(haystack))):
                if (needle[n_ptr] == haystack[h_ptr]):
                   n_ptr += 1
                   h_ptr += 1
                else:
                   h_ptr += 1
            if (n_ptr == len(needle)):
                return True
            return False
        Newd = sorted(d, key=functools.cmp_to_key(cmp))
        for word in Newd:
            if (compfunc (s,word)):
                return word
        return ""
