"""
1182. Shortest Distance to Target Color


You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

 

Example 1:

Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
Example 2:

Input: colors = [1,2], queries = [[0,3]]
Output: [-1]
Explanation: There is no 3 in the array.
 

Constraints:

1 <= colors.length <= 5*10^4
1 <= colors[i] <= 3
1 <= queries.length <= 5*10^4
queries[i].length == 2
0 <= queries[i][0] < colors.length
1 <= queries[i][1] <= 3
"""
import collections
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        def findClose(lt, idx):
            if len(lt) == 0:
                return -1
            mindis = float('inf')
            start, end = 0, len(lt)-1
            while(start <= end):
                mid = start + (end - start)//2
                if lt[mid] == idx:
                    return 0
                if lt[mid] > idx:
                    mindis = min(mindis, abs(idx-lt[mid]))
                    end = mid -1
                elif lt[mid] < idx:
                    mindis = min(mindis, abs(idx-lt[mid]))
                    start = mid + 1
            return mindis
        c = collections.defaultdict(list)
        
        # Keep track of the index where we saw the colors
        for idx in range(len(colors)):
            c[colors[idx]].append(idx)
        
        # For each query. search the colors and compute the distance
        ans = list()
        for query in queries:
            ans.append(findClose(c[query[1]], query[0]))
        return ans
            