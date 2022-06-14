"""
839. Similar String Groups

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
"""


""" 
Modified union find.. 
Go through all the strings and find the ones that are similar. 
link them up using union(u,v) Once done, go thorugh all the points and find the root.
The distinct number of nodes is the answer.
"""
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        # coding the business logic (similar strings)
        def similar(s1, s2):
            if s1 == s2:
                return True
            if len(s1) != len(s2):
                return False
            pair = set()
            for c1,c2  in zip(s1,s2):
                if c1 != c2:
                    if (c1, c2) in pair:
                        return
                    if (c2, c1) in pair:
                        pair.add((c2,c1))
                    pair.add((c1,c2))
            if len(pair) > 2:
                return False
            return True
        
        def find(u):
            if root[u] == u:
                return u
            # path compression
            root[u] = find(root[u])
            return root[u]
        
        def union(u,v):
            root_u = find(u)
            root_v = find(v)
            root[root_u] = root_v
            return 
        
        neigh = collections.defaultdict(set)
        root = [i for i in range(len(strs))]
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if similar(strs[i], strs[j]):
                    union(i,j)
                    
        # distinct roots
        roots  = set()
        for i in range(len(root)):
            roots.add(find(i))
        return len(roots)
            
        
                    
            