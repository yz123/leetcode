"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return 0
        #is leaf
        if node.left==None and node.right ==None:
            return 1
        elif node.left ==None:
            return 1+self.dfs(node.right)
        elif node.right == None:
            return 1+self.dfs(node.left)
        else:
            return 1+min(self.dfs(node.left), self.dfs(node.right) )
