"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #return self.iterative(root)
        return self.recursion(root)
    
    def recursion(self, root):
        res =[]
        
        if root:
            res = self.recursion(root.left)
            res +=  [root.val]
            res += self.recursion(root.right)
            #res = self.recursion(root.left) + [root.val] +self.recursion(root.right)
        return res
        
    
    def iterative(self, root):
        res = []
        node = root
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            if len(stack)==0:
                break
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
