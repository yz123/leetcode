"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        cur_layer = [root]
        res = [[root.val]]
        
        while True:
            tmp = []
            tmp_val =[]
            for node in cur_layer:
                if node.left:
                    tmp.append(node.left)
                    tmp_val.append(node.left.val)
                if node.right:
                    tmp.append(node.right)
                    tmp_val.append(node.right.val)
                   
            if len(tmp)==0:
                break
            cur_layer = tmp
            res.insert(0, tmp_val)
        
        return res
        
