# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = result = ListNode(0)

        while l1 and l2:
            if l1.val <= l2.val:
                result.next = ListNode(l1.val)
                l1 = l1.next
            else:
                result.next = ListNode(l2.val)
                l2 = l2.next
            result = result.next    
        result.next = l1 or l2

        return node.next
