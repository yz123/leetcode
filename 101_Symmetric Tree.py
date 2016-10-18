"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        """
        #recursive
        if root==None: return True
        return self.recursion(root.left, root.right)
        """
        
        """
        #iterative pre-order dfs
        return self.pre_dfs(root)
        """
        
        #iterative bfs
        return self.bfs(root)
    
    def bfs(self, root):
        if root == None: return True
        
        q = []
        q.append( (root.left, root.right) )
        while q:
            (l, r) = q.pop(0)
            if l == None and r == None:
                continue
            elif l and r and (l.val == r.val):
                q.append(  (l.left, r.right) )
                q.append( (l.right, r.left) )
            else:
                return False
        return True
    
    def pre_dfs(self, root):
        if root == None: return True
        
        stack = []
        stack.append( (root.left, root.right) )
        while stack:
            (l, r) = stack.pop()
            if l and r and (l.val ==r.val):
                stack.append( (l.right, r.left) )
                stack.append( (l.left, r.right)  )
            elif l==None and r==None:
                continue
            else:
                return False
        return True
    
    def recursion(self, l, r):
        if l==None and r == None:
            return True
        elif l and r:
            return l.val == r.val and (self.recursion(l.left, r.right) ) and (self.recursion(l.right, r.left))
        
        return False
