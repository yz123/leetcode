"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.recursion(p,q)
    
    def recursion(self, p, q):
        if q==None and p==None: return True
        if q and p and p.val ==q.val and self.recursion(p.left, q.left) and self.recursion(p.right, q.right): return True
        return False
