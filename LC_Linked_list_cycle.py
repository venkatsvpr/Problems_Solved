/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 * have two pointers. increement first once.. incremeent second twice. if they both meet then there is a cycle
 */
bool hasCycle(struct ListNode *head) 
{
    struct ListNode *p, *q;
    p = head;
    if (head == NULL)
    {
        return 0;
    }
    
    if ((head->next == NULL) || (head->next->next == NULL))
    {
        return 0;
    }
    q = head->next->next;
    
    while (q != NULL)
    {   
        if (p == q)
        {
            return 1;
        }
        if (q->next == NULL)
        {
            break;
        }
        
        p = p->next;
        q = q->next->next;
    }
    return 0;
    
}
