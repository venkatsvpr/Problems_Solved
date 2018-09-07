/*
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

    */

    /**
     * Definition for a binary tree node.
     * struct TreeNode {
     *     int val;
     *     struct TreeNode *left;
     *     struct TreeNode *right;
     * };
     */

    /*
    Straight Foward solution
    1) If  value is less than root value... call deltete node on left and update the return left pointer with the returned pointer
    2) if value is more than root vlaue.. call deltee node for right.. and update the right pointer with the returned pointer
    3) if it is equal.
        if (root.left is null):
        return root.right
        if (root.right is null):
        return root.left
        if both are present.
            the find the inorder successor(left most node of root.right)
            find it copy the value to the current node and delete that node.

    */
    struct TreeNode * inOrderSuccessor (struct TreeNode *root) {
        struct TreeNode *temp = root;
        while (temp->left != NULL) {
            temp = temp->left;
        }
        return temp;
    }
    struct TreeNode* deleteNode(struct TreeNode* root, int key) {
        if (root == NULL) {
            return NULL;
        }
        if (root->val < key) {
            root->right = deleteNode (root->right, key);
            return root;
        }
        else if (root->val > key) {
            root->left = deleteNode (root->left, key);
            return root;
        }
        else {
            if (root->right == NULL) {
                struct TreeNode *temp = root->left;
                free(root);
                return temp;
            }
            if (root->left == NULL) {
                struct TreeNode *temp = root->right;
                free(root);
                return temp;
            }
            struct TreeNode *succ = inOrderSuccessor (root->right);
            if (succ == NULL) {
                return NULL;
            }
            root->val = succ->val;
            root->right = deleteNode(root->right, succ->val);
        return root;
        }
    }
