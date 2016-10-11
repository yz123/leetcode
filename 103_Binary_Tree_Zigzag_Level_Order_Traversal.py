"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q = []
        q.append(root)
        i=0
        res = []
        while q:
            #q
            tmp=[]
            output = []
            if i %2 ==0:
                for node in q:
                    output.append(node.val)
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
            #stack
            if i%2 !=0:
                for node in q:
                    output.insert(0, node.val)
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
            res.append(output)
            q = tmp
            i+=1
        return res        
