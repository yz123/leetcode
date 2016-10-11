"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #return self.dfs(root, None, None)
        return self.dfs1(root, -9999999999999, 999999999999999)
        #return self.inorder(root)
    
    def dfs(self, root, minNode, maxNode):
        if not root: return True
        
        #if not root.left and not root.right: return True
        
        if minNode and root.val <=minNode.val:
            return False
        
        if maxNode and root.val >=maxNode.val:
            return False
        
        return self.dfs(root.left, minNode, root) and self.dfs(root.right, root, maxNode)
    
    def dfs1(self, root, minv, maxv):
        if not root: return True
        if root.val >= maxv or root.val <=minv: return False
        return self.dfs1(root.left, minv, root.val) and self.dfs1(root.right, root.val, maxv)
        
    def inorder(self, root):
        if not root: return True
        pre = None
        node = root
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not stack: break
            node = stack.pop()
            #print  pre, node.val
            #print pre>=node.val
            if pre!=None and pre >= node.val:
                return False
            else:
                pre = node.val
            node = node.right
            
        return True
        
        
        
