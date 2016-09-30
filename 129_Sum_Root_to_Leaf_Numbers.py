"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#BFS
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        q = []
        q.append( (root, root.val) )
        sum = 0
        while q:
            (node, cur_val) =q.pop(0)
            if node.left == None and node.right == None:
                sum += cur_val
            if node.left!=None:
                q.append( (node.left, cur_val*10+node.left.val) )
            if node.right!=None:
                q.append( (node.right, cur_val*10+node.right.val) )
        return sum
        
