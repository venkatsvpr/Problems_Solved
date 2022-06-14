"""

239. Sliding Window Maximum


You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        d = list()
        out = []
        for i, n in enumerate(nums):
            if (d):
                # pop stored indexes that are not of use to us.
                if d[0] <= i - k:
                    d.pop(0)

            # pop all the elements from the end that are less than the current element
            while d and nums[d[-1]] < n:
                d.pop()
            # append the current element
            d.append(i)

            # from k-1 start appending the start of d, which is the biggest number to the output.
            if i >= k-1:
                out += nums[d[0]],
        return out


import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        output = []
        l = r = 0
        
        while r < len(nums):
            # pop out from top entries that are smaller than current num
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            # add current num  idx to the dq
            q.append(r)
            
            # Check if  the size is reached
            if (r - l +1) >= k:
                output.append(nums[q[0]])
                l += 1
                
                # If some numbers have become invalid. pop them out
                if l > q[0]:
                    q.popleft()
            r += 1
        return output
                
            
                
        
       