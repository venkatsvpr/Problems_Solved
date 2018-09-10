"""
Interesting one.

Create a dictionary to the store the running sum .. with the frequency.
At every point if (runningsum-k) is there on the dictionary.. that means.. difference between current running sum and older running sum is k.
means.. sum of elemments form the end of that array to this array is k.. which is what we want...
add the frequency of that subarry to the Answer.

A less efficent way would be to store the running sum in a array. for every new running sum... loop through all the old elements and keep track how many elements have a difference of k



Approach:
=========
1) We attempt it by the running sum
2) at evey element have a dict for the running sum.. if running sum is already present increment the count. else insert with count 1
3) at every step check if runningsum-k is there on the dict.. if it is there add the number of times it is present to the count.
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running = dict()
        rsum = 0
        running[0] = 1
        count = 0
        for num in nums:
            rsum += num
            if (rsum - k ) in running:
                count += running[rsum-k]
            if (rsum in running):
                running[rsum] += 1
            else:
                running[rsum] = 1
        print (running)
        return count
