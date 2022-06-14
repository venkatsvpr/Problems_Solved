"""
1202. Smallest String With Swaps


You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.

"""


"""
- Keep track of the connected pairs
- All connected nodes can be moved form anywhere to anywhere.

"""
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        root = [i for i in range(len(s))]
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(u,v):
            rootu = find(u)
            rootv = find(v)
            
            root[rootu] = rootv
            return
        
        # Perform union find
        for [u,v] in pairs:
            union(u,v)
        
        #keep track of root-node and all the characters in the connected component
        m = collections.defaultdict(list)
        for i in range(len(s)):
            m[find(i)].append(s[i])
        
        # Create an iterator, insstead of sorted we can do bucket sort
        iterm = dict()
        for k in dict(m):
            iterm[k] = iter(sorted(m[k]))
        
        # go through nodes, get the root-node and pull a character from the iterator
        ans = ""
        for i in range(len(s)):
            ans += next(iterm[root[i]])
        return ans
            
        
            
            
        
        
        
        
        
            
            