"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #return self.resursion(root)
        return self.inorder_traverse(root)
    
    def inorder_traverse(self, root):
        if not root: return 0
        max_layer = 1
        level = 1
        node = root
        stack = []
        while True:
            while node:
                stack.append( (node, level))
                node = node.left
                level+=1
            if len(stack) == 0:
                break
            (node, level) = stack.pop()
            if node.left == None and node.right == None:
                if max_layer < level:
                    max_layer = level 
            node = node.right
            level +=1
        return max_layer
            
    def resursion(self, root):   
        if not root: return 0
        if root.left==None and root.right == None:
            return 1
        
        return 1+ max( self.maxDepth(root.left), self.maxDepth(root.right))
