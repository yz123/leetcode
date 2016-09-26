"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#two pointer, one move one step; the other move two steps
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        one = head
        two = head
        while two != None and two.next != None:
            two = two.next.next
            one = one.next
            if one == two:
                return True
        
        return False
