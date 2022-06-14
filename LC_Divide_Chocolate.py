"""

1231. Divide Chocolate

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

 

Example 1:

Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
Example 2:

Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There is only one way to cut the bar into 9 pieces.
Example 3:

Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
 

Constraints:

0 <= k < sweetness.length <= 104
1 <= sweetness[i] <= 105
"""

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # check the number of pieces we can make ensuring the sweetness does not go below the level
        def maxpieces(minsweet):
            pieces = 1
            sweet = 0
            for i in sweetness:
                sweet += i
                if sweet >= minsweet:
                    sweet = 0
                    pieces += 1
            if sweet < minsweet:
                pieces -= 1
            return pieces
        
        # The search space is ranging from me picking up the minimum piece to sum of all piece
        left,right = min(sweetness), sum(sweetness)
        ans = right
        while(left <= right):
            mid = left + ((right - left)//2)
            p = maxpieces(mid)
            # We need k+1 pieces, anything less we have cut too big.. reduce the sweetness to increase the piece
            if p < k  + 1:
                right = mid - 1
            else:
                left = mid + 1
        return right