"""
862. Shortest Subarray with Sum at Least K

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.



Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3


Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
Approach:
==========

1) Store the running sum in sum_array
2) Iterate through the running sum and push the index of the sum into a Queue if empty.
3) If not empty.. try to pop elements which are bigger than the current running sum from the append
   Calculate the difference between the first element in queue and the current running sum.
   If this is greater than k. calcualte the mininum.
   At the end insert idx into the Queue

"""


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        running_sum = 0
        sum_array = [0]
        for item in A:
            running_sum += item
            sum_array.append(running_sum)

        Queue = []
        minlen = len(A)+1
        for idx,value in enumerate(sum_array):
            # pop elements from the end.. since we have smaller elements
            # the bigger elements doesnt make sense
            while (Queue) and (value <= sum_array[Queue[-1]]):
                Queue.pop()

            # calculate the difference between the first element of the queue (min sum element)
            # and current element
            while (Queue) and (value - sum_array[Queue[0]] >= K):
                minlen = min(minlen, idx-Queue[0])
                Queue.pop(0)
            Queue.append(idx)
        # sum k not reached case
        if (minlen == len(A)+1):
            return -1
        return (minlen)
