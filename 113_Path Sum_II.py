"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#similar to 131, 140
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        """
        self.res = []
        self.dfs1(root, sum, [])
        return self.res
        """
        
        return self.dfs(root, sum)
        
    
    
    def dfs1(self, root, sum, path):
        if not root:
            return []
        if root.left == None and root.right == None and 0 == sum-root.val:
            self.res.append(path+[root.val])
        
        if root.left:
            self.dfs1(root.left, sum-root.val, path+[root.val])
        if root.right:
            self.dfs1(root.right, sum-root.val, path+[root.val])
    
    def dfs(self, root, sum):
        if not root:
            return []
        res = []
        if root.left == None and root.right == None and 0 == sum - root.val :
            #print "XX"
            return [ [root.val]]
        
        if root.left:
            l_list = self.dfs(root.left, sum-root.val)
            for node in l_list:
                res.append( [root.val]+node )
        if root.right:
            r_list = self.dfs(root.right, sum-root.val)
            for node in r_list:
                res.append( [root.val]+node )
        return res
