# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Find the kth node from the end. 
# Connect the k-1th node to None. 
# Connect the end node to the head.
# Kth node is the head
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (head is None):
            return None

        if ((head.next == None) or (k==0)):
            return head

        fast = head
        slow = head
        
        temp = ListNode(0);
        temp = head
        count = 0;
        while (fast != None):
            fast = fast.next
            count += 1
        
        k = k % count;
        if (k == 0):
            return head
        
        fast = head
        for i in range(0,k):
            fast = fast.next
        
        while (fast.next != None):
            fast = fast.next
            slow = slow.next
        temp = slow
        slow = slow.next
        temp.next = None;
        fast.next = head;
        return slow;
