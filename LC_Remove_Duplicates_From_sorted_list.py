  """
  Given a sorted linked list, delete all duplicates such that each element appear only once.

  Example 1:

  Input: 1->1->2
  Output: 1->2
  Example 2:

  Input: 1->1->2->3->3
  Output: 1->2->3
  """

  # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def del_next(node):
            nxt = node.next.next
            del(node.next)
            node.next = nxt
        node = head
        while (node != None):
            if (node.next == None):
                break;
            elif (node.val == node.next.val):
                del_next(node)
            else:
                node = node.next
        return head
