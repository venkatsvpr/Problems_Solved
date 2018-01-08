"""
There are three colors. The cost of picking a color for nth house .. 
Is cost of picking a color to nth house and the min cost of picking other two colors for n-1 th house.
We will choose the minimum value from the different colors for any particular house.
"""
class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        if not costs:
            return 0;
        N = len(costs)
        """
        cost for painting a c
        """
        for i in range(1,N):
            costs[i][0] = costs[i][0] + min (costs[i-1][1], costs[i-1][2]);
            costs[i][1] = costs[i][1] + min (costs[i-1][0], costs[i-1][2]);
            costs[i][2] = costs[i][2] + min (costs[i-1][0], costs[i-1][1]);
        return (min(costs[N-1]))
