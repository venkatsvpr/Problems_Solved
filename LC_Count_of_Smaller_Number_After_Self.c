// Count of Smaller Numbers After Self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
typedef struct Node{
    struct Node *left;
    struct Node *right;
    int value;
    int less_count;
    int batch_count;
    bool visited;
}Node;


Node *head;

Node *
CreateNode (int num)
{
    Node *new_node = (Node *) malloc(sizeof(Node));
    new_node->right = NULL;
    new_node->left =NULL;
    new_node->less_count = 0;
    new_node->batch_count = 0;
    new_node->value = num;
    new_node->visited = false;
    return new_node;
}

int
find_less_count (Node *root, int value)
{
    if (root == NULL)
        return 0;
    
    if (root->batch_count > 0)
    {
        update_less_count(root,root->batch_count); 
        root->batch_count = 0;
    }
    
    if (root->value == value)
    {
        if (root->visited == true)
        {
            return (find_less_count(root->right, value));
        }
        root->visited = true;
        return root->less_count;
    }
    else if (root->value < value)
    {
        return (find_less_count (root->right, value));
    }
    else
    {
        return(find_less_count (root->left, value));
    }
    return 0;
}   


void update_less_count(Node *node, int count)
{
    if (node == NULL)
        return;
    
    node->less_count = node->less_count + count;
    update_less_count(node->left, count);
    update_less_count(node->right, count);
}

void batch_update_less_count (Node *node)
{
    if (node == NULL)
        return;
    
    node->batch_count++;
    return;
}

void
insert (Node *root, Node *new_node)
{
    if (root->batch_count > 0)
    {
        update_less_count(root, root->batch_count);
        root->batch_count = 0;
    }
    if (new_node->value > root->value)
    {
        if(root->right== NULL)
        {
            root->right = new_node;
        }
        else
        {
            insert (root->right, new_node);
        }
    }
    else if (new_node->value < root->value)
    {
        batch_update_less_count(root->right);
        root->less_count++;
        if (root->left == NULL)
        {
            root->left = new_node;
        }
        else
        {
            insert(root->left, new_node);
        }        
    }
    else if (new_node->value == root->value)
    {  
        if (root->right == NULL)
        {
            root->right = new_node;
        }
        else
        {
            insert(root->right, new_node);
        }        
    }
    return;
}

int* countSmaller(int* nums, int numsSize, int* returnSize) 
{
    head = NULL;
    
    if (nums == NULL)
        return NULL;
    
    if (numsSize == 0)
        return NULL;

    if (head== NULL)
    {
        head = CreateNode(nums[0]);
    }       
    
    for (int i =1;i<numsSize; i++)
    {
        insert(head, CreateNode(nums[i])); 
    }
    
    int *result = malloc(numsSize * sizeof(int));
    *returnSize = numsSize;
    for (int i= 0; i <numsSize; i++)
    {
        result[i] = find_less_count(head,nums[i]);
    }
    return  result;
}

