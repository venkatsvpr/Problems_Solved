"""
915. Partition Array into Disjoint Intervals

Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.


Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]

We are looking for a pattern that the all elements in left is less than or equal to every element in right array.
the way we solve this is by picking the max element in left array which is less than or  equal to min of the right array.
have a running max from left and running min from right side.
go through this array and find the first one where an element from max is less than or equal to the next element in min.
just find this spot.

since it is askeed that the left array be of the least size we are returning at the first occurance of such.

"""
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxleft = [None]*len(A)
        minright  = [None]*len(A)
        maxleft[0] = A[0]
        for i in range(1,len(A)):
            maxleft[i] = max(maxleft[i-1],A[i])

        minright[len(A)-1] = A[-1]
        for i in range(len(A)-2,-1,-1):
            minright[i]= min(A[i],minright[i+1])

        for i in range(len(A)-1):
            if (maxleft[i] <= minright[i+1]):
                return i+1
        return -1
