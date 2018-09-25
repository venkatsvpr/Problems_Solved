"""
80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

"""
Approach: Have two pointers.. once is the current pointer
other is the index where we should update in place.
store the prev value and see if we have the number for once and twice.
once we see a different character commit the prev character with the ffrequencey.

seenOnce is a set that tracks the characters that came once.
seenTwice is a set to track the characters that came twice.

We could have just set  a flag to keep track of the single and double character case.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seenOnce = set()
        seenTwice = set()
        idx = 0
        end = 0
        prev = None
        while (end < len(nums)):
            if (prev == None):
                prev = nums[end]
                seenOnce.add(nums[end])
            elif (prev != None):
                if (prev == nums[end]):
                    if (nums[end] not in seenOnce):
                        seenOnce.add(nums[end])
                    else:
                        seenTwice.add(nums[end])
                else:
                    if (prev in seenOnce):
                        nums[idx] = prev
                        idx += 1
                    if (prev in seenTwice):
                        nums[idx] = prev
                        idx += 1
                    prev = nums[end]
                    seenOnce.add(nums[end])
            end += 1
        if (prev in seenOnce):
            nums[idx] = prev
            idx += 1
        if (prev in  seenTwice):
            nums[idx] = prev
            idx += 1
        return idx
