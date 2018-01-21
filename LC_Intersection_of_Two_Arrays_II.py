"""
Create counter for nums1,nums2
Find the overlap and elements
"""
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = collections.Counter(nums1)
        b = collections.Counter(nums2)
        return list((a&b).elements())
