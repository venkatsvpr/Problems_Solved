/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode * rec_flatten(struct TreeNode * root)
{
    struct TreeNode *retval = NULL;
    struct TreeNode *temp = NULL;
    
    if (root == NULL)
    {
        //printf ("returning null \r\n");
        return NULL;
    }
    
    struct TreeNode *left, *right;
    left = root->left;
    right = root->right;
 //   printf  ("<%s:%d> <%d>\r\n",__func__,__LINE__,root->val);

    retval = rec_flatten (left);
    if (retval != NULL)
    {
        temp = retval;
        while (temp->right)
        {
            temp = temp->right;
        }       
        temp->right = root->right;
        root->left = NULL;
        root->right = retval;
    }
    retval = rec_flatten(right);
    return (root);    
}
void flatten(struct TreeNode* root) 
{
    rec_flatten (root);
}


