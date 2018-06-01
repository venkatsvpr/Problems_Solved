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
