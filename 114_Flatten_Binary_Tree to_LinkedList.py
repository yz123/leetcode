"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Subscribe to see which companies asked this question
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #iterative
    def flatten(self, root):
        self.iterative(root)
        #self.flatten1(root)
    
    def iterative(self, root):
        if not root:
            return 
        stack = []
        cur = root
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if node!=root:
                cur.right = node
                cur = cur.right
            node.right = None
            node.left =None   

    
    #recursion
    #先处理左子树，然后指针指向左子树最后，然后右子树，然后链上
    def flatten1(self, root):
        if not root:
            return 
        cur = root
        if root.left:
            self.flatten1(root.left)
            node = root.left
            cur = node
            while node.right:
                node = node.right
                cur = node
                
        if root.right:
            self.flatten1(root.right)
            cur.right = root.right
        if root.left:
            root.right = root.left
            root.left = None
        
