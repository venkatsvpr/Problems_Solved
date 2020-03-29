"""
1395. Count Number of Teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
"""
"""
Do dfs also memoize sub problem answers
"""
class Solution(object):
    Ans = 0
    memo = dict()
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        def rec(idx, inc, currentVal, curLength):
            if (idx,inc,curLength) in self.memo:
                self.Ans += self.memo[(idx, inc, curLength, currentVal)]
                return True
            if (currentVal > 0):
                if (inc == True and rating[idx] < currentVal):
                    return False
                if (inc == False and rating[idx] > currentVal):
                    return False
            if (curLength == 2):
                if (inc == True and rating[idx] > currentVal):
                    self.Ans += 1
                    self.memo[(idx, inc, curLength, currentVal)] = 1
                    return True
                if (inc == False and rating[idx] < currentVal):
                    self.Ans += 1
                    self.memo[(idx, inc, curLength, currentVal)] = 1
                    return True
            count = 0
            path = 0
            for futureIdx in range(idx+1, len(rating)):
                if (rec(futureIdx, inc, rating[idx], curLength + 1)):
                    count += 1
                    path += self.memo[(futureIdx, inc, curLength+1, rating[idx])]
            if (count > 0):
                self.memo[(idx,inc,curLength, currentVal)] = path
                return True
        for idx in range(0, len(rating)-1):
            rec(idx, True, -1, 0)
            rec(idx, False, -1, 0)
        return self.Ans
        