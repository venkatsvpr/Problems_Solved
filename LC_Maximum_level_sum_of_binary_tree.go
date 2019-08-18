```
1161. Maximum Level Sum of a Binary Tree
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 

Example 1:



Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
 

Note:

The number of nodes in the given tree is between 1 and 10^4.
-10^5 <= node.val <= 10^5
```
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxLevelSum(root *TreeNode) int {
    AnsMap := make(map[int]int)
    if (root != nil) {
        recLevel(root, AnsMap, 1)
    }
    ans := int(0)
    akey := int(-1)
    for key,value := range(AnsMap) {
        if (value > ans) {
            ans = value
            akey = key
        }
    }
    if (akey == -1) {
        return -1
    }
    return akey
}

func recLevel(root *TreeNode, m map[int]int, level int) {
    m[level] += root.Val 
    if (root.Left != nil) {
        recLevel(root.Left, m, level+1)
    }
    if (root.Right != nil) {
        recLevel(root.Right, m, level+1)
    }
}