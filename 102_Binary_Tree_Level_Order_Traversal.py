"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        return self.bfs(root)
    
    def bfs(self, root):
        if not root: return []
        
        res = []
        q = []
        q.append(root)
        while q:
            ele = []
            q_tmp =[]
            for node in q:
                ele.append(node.val) 
                if node.left:
                    q_tmp.append(node.left)
                if node.right:
                    q_tmp.append(node.right)
            res.append(ele)
            q = q_tmp
        return res
        
