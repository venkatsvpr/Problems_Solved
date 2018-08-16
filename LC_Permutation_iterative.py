"""
46. Permutations


Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
"""
At ever step add the elements to iteration. at every step
1 , [1]
2.,  [2,1] [1,2]
3,  [3 2 1] [ 2 3 1 ] [2 1 3 ] [ 3 1 2 ] [ 1 3 2 ] [ 1 2 3 ]
"""
class Solution(object):
    def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return perms
