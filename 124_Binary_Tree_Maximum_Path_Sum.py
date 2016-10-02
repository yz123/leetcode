"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#https://shenjie1993.gitbooks.io/leetcode-python/content/124%20Binary%20Tree%20Maximum%20Path%20Sum.html
#http://www.cnblogs.com/yrbbest/p/4438479.html
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.maxsum = root.val
        
        #dfs return 从root到它子树的路径最大值, 等于return max(root.value, root.value + max(dfs(root.left), dfs(root.right)))
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            
            max_path = max(root.val, root.val+max(l, r))
            self.maxsum = max( self.maxsum, root.val + l+r, max_path  )
            
            return max_path
            
        dfs(root)
        return self.maxsum
        
