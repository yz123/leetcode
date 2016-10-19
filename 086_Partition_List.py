"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        return self.one_dummy(head, x)
        
        """
        #two head and then merge
        return self.two_head(head,x)
        """
    
    def one_dummy(self, head, x):
        dummy = ListNode(0)
        dummy.next = head
        cur_insert = dummy
        while cur_insert.next and cur_insert.next.val < x:
            cur_insert = cur_insert.next
            
        p = cur_insert.next
        if p: 
            while p.next:
                if p.next.val >= x:
                    p = p.next
                else:
                    node = p.next
                    p.next = node.next
                    node.next = cur_insert.next
                    cur_insert.next = node
                    cur_insert = cur_insert.next
        
        return dummy.next
    
    def two_head(self, head, x):
        if head == None or head.next == None: return head
        
        small = ListNode(0)
        large = ListNode(0)
        
        p = head
        sp, lp = small, large
        while p:
            if p.val < x:
                sp.next = p
                sp = sp.next
            else:
                lp.next = p 
                lp = lp.next
            p = p.next
        
        sp.next = large.next
        lp.next = None
        return small.next
        
