"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddEnd = None
        evenEnd = None
        oddStart = None
        evenStart = None
        node = head
        def insert_end (end,a):
            a.next = end.next
            end.next = a
            return a
        if head is None:
            return None
        count = 0
        while (node != None):
            nxt = node.next
            if (oddEnd == None):
                if (count % 2 != 0):
                    oddEnd = node
                    oddStart = node
                    node = node.next
                    count += 1
                    continue;
            if (evenEnd == None):
                if (count % 2 == 0):
                    evenEnd = node
                    evenStart = node
                    node = node.next
                    count += 1
                    continue;
            if (count %2 == 0):
                evenEnd = insert_end (evenEnd, node)
            else:
                oddEnd = insert_end (oddEnd, node)
            node = nxt
            count += 1

        if (evenEnd != None):
            evenEnd.next= oddStart

        if (oddEnd != None):
            oddEnd.next = None
        return evenStart
