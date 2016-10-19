"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        cur = head
        while  cur and cur.next:
            if cur.val != cur.next.val:
                cur = cur.next
                pre = pre.next
            else: #cur.val == cur.next.val
                end = cur.next
                while end and end.val == cur.val:
                    end = end.next
                if end==None:
                    pre.next =None
                    break
                pre.next = end
                cur = end
        
        return dummy.next            
                    
