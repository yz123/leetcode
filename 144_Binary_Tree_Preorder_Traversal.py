"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        stack = []
        if root !=None:
            node = root
            while True:
                while node!=None:
                    list.append(node.val)
                    stack.append(node)
                    node = node.left
                if len(stack)==0:
                    break
                node = stack.pop()
                node = node.right
        return list
    
    """
    def preorderTraversal(self, root):
        list = []
        if root!=None:
            list.append(root.val)
            list += self.preorderTraversal(root.left)
            list += self.preorderTraversal(root.right)
        return list
    """
