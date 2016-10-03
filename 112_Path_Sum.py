"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.preorder(root, sum)
        #return self.dfs(root, sum, 0)
        #return self.bfs(root, sum)
        
    def preorder(self, root, sum):
        if not root:
            return False
        parent_val = 0
        stack = [ (root, parent_val)]
        while stack:
            (node, parent_val) = stack.pop()
            cur_val = node.val + parent_val
            if cur_val == sum and node.left ==None and node.right ==None:
                return True
            if node.right:
                stack.append( (node.right, cur_val) )
            if node.left:
                stack.append( (node.left, cur_val) )
        return False
        
        
    def dfs(self, node, sum, parentsum):
        if not node:
            return False
            
        if node.left==None and node.right == None:
            if node.val + parentsum == sum:
                return True
            else:
                return False
        if self.dfs(node.left, sum, node.val+parentsum) or self.dfs(node.right, sum, node.val+parentsum):
            return True
            
        return False
    
    def bfs(self, root, sum):
        if not root:
            return False
        q =[ (root, 0) ] #(root, parent_sum)
        while q:
            next_q = []
            for i in range(len(q)):
                (node, parentsum) = q[i]
                cursum = node.val + parentsum
                if  cursum == sum and node.left==None and node.right==None:
                    return True
                if node.left:
                    next_q.append( (node.left, cursum)  )
                if node.right:
                    next_q.append( (node.right, cursum)  )
            q = next_q
        return False
