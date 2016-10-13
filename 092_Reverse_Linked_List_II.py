"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n : return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        i=1
        while i<m:
            pre = pre.next
            i+=1
        cur = pre.next
        i = m
        #print pre.val
        while i<n:
            print cur.next.val
            moved = cur.next
            cur.next = moved.next
            moved.next = pre.next
            pre.next = moved
            i+=1
        
        return dummy.next
        
