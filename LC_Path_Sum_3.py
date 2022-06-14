"""
437. Path Sum III


Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Perform pre order traversal and keep computing the prefix sum
- This will be used to compuate at any point of time there could be two types of answers
1) We have made a sum that equals target sum
2) We can make target sum with the previous prefix sums

"""
class Solution:
    def __init__(self):
        self.ans = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def traverse(node, curr_sum):
            nonlocal count
            if node == None:
                return
            
            curr_sum += node.val
            # Check the first condition
            if curr_sum == targetSum:
                count += 1
            
            # The check the prefix sums
            if d[curr_sum - targetSum] > 0:
                count += d[curr_sum - targetSum]
            
            # Keep track of the current sum for the future use
            d[curr_sum] += 1
            traverse(node.left, curr_sum)
            traverse(node.right, curr_sum)
            # Discard the current sum
            d[curr_sum] -=1
            return
        d = defaultdict(int)
        count = 0
        traverse(root, 0)
        return count