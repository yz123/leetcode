"""
Sort a linked list using insertion sort.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        cur = head.next
        head.next = None
        dummy = ListNode(None)
        dummy.next = head
        while cur:
            tmp = cur.next
            start = dummy
            while start.next and start.next.val <= cur.val:
                start= start.next
            cur.next = start.next
            start.next =cur
            cur = tmp
        return dummy.next
