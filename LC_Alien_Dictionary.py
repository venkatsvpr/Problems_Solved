"""
269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
"wrt",
"wrf",
"er",
"ett",
"rftt"
]

Output: "wertf"
Example 2:

Input:
[
"z",
"x"
]

Output: "zx"
Example 3:

Input:
[
"z",
"x",
"z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
"""
Approch:
use the data and create a graph for word1, word2
if c1,c2 same..continue.
else.. add it graph and break
do a topological sort on the graph and create the order
"""
import collections
class Tree(object):
    def __init__(self,char):
        self.content = char
        self.value = 1;
        self.child = []

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # do a dfs and if we find a loop return false
        def dfs (item, Visited, Ans,treeMap):
            Visited[item] = 1
            if (0 == len(treeMap[item].child)):
                Ans.append(item)
                Visited[item] = 2
                return True
            for child in treeMap[item].child:
                if (Visited[child.content] == 1):
                    return False
                if (Visited[child.content] == 2):
                    continue;
                if (False == dfs(child.content, Visited, Ans, treeMap)):
                    return False
            Visited[item] = 2
            Ans.append(item)
            return True

        charTreeMap = dict()
        prevword = None
        Visited = dict()
        for word in words:
            for char in word:
                Visited[char] = 0
                if (char not in charTreeMap):
                    charTreeMap[char] = Tree(char)
        prevword = None

        # create a linking
        for word in words:
            if (prevword == None):
                prevword = word
                continue
            minlen = min(len(prevword),len(word))+1
            for c1,c2 in zip(prevword[:minlen],word[:minlen]):
                if (c1 == c2):
                    continue;
                charTreeMap[c1].child.append(charTreeMap[c2])
                break;
            prevword = word
        Ans = []

        # do a topological sort kind of thing
        for ch in Visited:
            if (Visited[ch] == 0):
                if (False == dfs(ch,Visited, Ans, charTreeMap)):
                    return ""
        return "".join(reversed(Ans))
    



import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        ## Create a adjaceny list
        adj = collections.defaultdict(set)
        
        # Create an entry for all the characters
        for word in words:
            for ch in word:
                adj[ch] = set()
        
        ## Check for words that break the rule of length
        for j in range(len(words)-1):
            w1,w2 = words[j], words[j+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        # We use the visited to keep track of two states.
        # Visit with value true means it is in the path, false means we are done with it.
        visit = dict()
        ans = []
        
        # Perform post order travesal
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for nei in adj[c]:
                # Detect loops
                if dfs(nei):
                    return True
            visit[c] = False
            ans.append(c)
        
        for ch in dict(adj):
            # Check for loop
            if dfs(ch):
                return ""
        return "".join(ans[::-1])
                
        
    