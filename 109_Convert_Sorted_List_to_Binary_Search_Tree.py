"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#http://bangbingsyb.blogspot.com/2014/11/leetcode-convert-sorted-list-to-binary.html
#http://www.cnblogs.com/yrbbest/p/4437320.html
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        #return self.findmiddle(head)
        return self.bottom_up(head)
    
    """
    #找中点，再递归算法
    def findmiddle(self, head):
        if head == None:
            return None
        
        #find middle node
        slow, fast, pre = head, head, head
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        root = TreeNode(slow.val)
        #build right
        root.right = self.findmiddle(slow.next)
        
        pre.next = None
        #build left
        if slow!= head:
            root.left = self.findmiddle(head)
        
        return root
    """
    
    #自底向上的方法
    def bottom_up(self, head):
        if head == None: return None
        
        cur, num = head, 1
        while cur.next:
            cur = cur.next
            num += 1
        begin, end = 0, num-1
        self.cur = head
        return self.inorder(self.cur, begin, end)
    
    #in-order traversal
    def inorder(self, head, begin, end):
        
        if begin > end: return None
        
        middle = begin + (end - begin)/2
        
        #traverse left
        left = self.inorder(self.cur, begin, middle-1) 
        
        #visit the middle
        root = TreeNode( self.cur.val )
        self.cur = self.cur.next   #move the cur pointer to the next element 
        
        #traverse right
        right = self.inorder(self.cur, middle+1, end)
        
        root.left = left
        root.right = right
        
        return root
        
