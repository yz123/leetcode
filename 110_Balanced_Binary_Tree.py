"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        """
        #return two value: isbalanced, height
        (isBalanced, height) = self.dfs(root)
        return isBalanced
        """
        
        return self.dfs_height(root)!=-1
    
    #return -1 if it is not balanced, else get height    
    def dfs_height(self, root):
        if not root:
            return 0
        l = self.dfs_height(root.left)
        r = self.dfs_height(root.right)
        if l == -1 or r ==-1 or abs(l-r)>1:
            return -1
        else:
            return 1+max(l, r)
        
    #return (isBalanced, height)
    def dfs(self, root):
        if not root:
            return (True, 0)
        (isBal_left, lheight) = self.dfs(root.left)
        if not isBal_left:
            return (False, -1)
            
        (isBal_right, rheight) = self.dfs(root.right)
        if not isBal_right:
            return (False, -1)
        
        return (  abs(lheight-rheight)<=1, 1+max(lheight, rheight))
