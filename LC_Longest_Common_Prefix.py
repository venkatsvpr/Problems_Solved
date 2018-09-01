"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isData  = False

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        root  = TrieNode()
        save = root
        st = ""
        for word in strs:
            root = save
            if (len(word) == 0):
                return st
            for ch in word:
                root = root.children[ch]
            root.isData = True

        root = save
        while ((len(root.children) == 1) and (root.isData == False)):
            for key in root.children:
                st += key
            root  = root.children.get(key)
            if (root == None):
                break;

        return st
    
