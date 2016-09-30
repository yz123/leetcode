"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
For example,
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = 12 + 13 = 25.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#dfs
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #return self.bfs(root)
        #return self.dfs(root, 0)
        #return self.dfs_middleorder(root)
        return self.dfs_preorder(root)
    
    #dfs
    def dfs(self, node, cur):
        
        if node==None:
            return 0
        
        cur = 10*cur + node.val
        #print cur
        if node.left==None and node.right==None:
            return cur
        
        sum = 0
        if node.left:
            sum += self.dfs(node.left,cur)
        if node.right:
            sum += self.dfs(node.right, cur)
        return sum
        
    #dfs:iterative
    def dfs_middleorder(self, root):
        if root == None:
            return 0
        stack = []
        node = root
        cur = 0
        sum = 0
        while True:
            while node:
                cur = cur*10+node.val
                stack.append( (node, cur) )
                if node.left==None and node.right ==None:
                    sum+=cur
                node = node.left
            if not stack:
                break
            (node, cur) = stack.pop()
            node = node.right
        return sum
    
    #def:preorder
    def dfs_preorder(self, root):
        if root == None:
            return 0
        stack = []
        sum = 0
        stack.append( (root, root.val))
        while stack:
            (node, cur) = stack.pop()
            
            if node.right:
                stack.append( (node.right, 10*cur+node.right.val))
            if node.left:
                stack.append( (node.left, 10*cur+node.left.val))
            if node.left==None and node.right == None:
                sum+= cur
            
        return sum   
            
        
    #bfs
    def bfs(self, root):
        if root==None:
            return 0
        q = []
        q.append( (root, root.val) )
        sum = 0
        while q:
            (node, cur_val) =q.pop(0)
            if node.left == None and node.right == None:
                sum += cur_val
            if node.left!=None:
                q.append( (node.left, cur_val*10+node.left.val) )
            if node.right!=None:
                q.append( (node.right, cur_val*10+node.right.val) )
        return sum
