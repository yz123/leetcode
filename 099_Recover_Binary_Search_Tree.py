"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        #self.iterative_naive(root)
        
        """
        self.first, self.second, self.prenode = None, None, None
        self.inorder_recursion(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        """
        
        self.morris_traversal(root)
        
        
    #http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
    #http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
    #idea: 如果当前节点左子树为空，访问node， 否则将当前node移到左子树的最右边; 如果最右边遍历到当前节点，则将最右边那个设为None，移到当前的右边
    def morris_traversal(self, root):
        if not root: return None
        pre, cur = None, root
        first, second, before = None, None , None
        while cur:
            if cur.left ==None:
                
                #print cur.val
                if before and before.val >= cur.val:
                    if first!=None:
                        second = cur
                    else: #first == None
                        first = before
                        second = cur
                before = cur
                        
                cur = cur.right
            else:
                pre = cur.left
                
                while pre.right!=None and pre.right!= cur:
                    pre = pre.right
                    
                if pre.right == None:
                    pre.right = cur
                    cur = cur.left
                else: #pre.next = cur
                    pre.right = None
                    
                    #print cur.val
                    if before and before.val >= cur.val:
                        if first!=None:
                            second = cur
                        else: #first == None
                            first = before
                            second = cur
                    before = cur
                
                    cur = cur.right
                    
        first.val, second.val = second.val, first.val  
        
    def inorder_recursion(self, root):
        if not root: return None
        self.inorder_recursion(root.left)
        if self.prenode:
            if self.prenode.val >= root.val:
                #first is found
                if self.first:
                    self.second = root
                #first is not found
                else:
                    self.first = self.prenode
                    self.second = root
                
        self.prenode = root        
        self.inorder_recursion(root.right)
    
    #inorder traverse
    def iterative_naive(self, root):
        if not root: return None
        
        first, second, pre = None, None, None
        node = root
        stack = []
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not stack: break
            
            node = stack.pop()
            #if pre:
            #    print node.val, pre.val
            #travser node
            if pre and pre.val >= node.val:
                if first:
                    second = node
                    break
                else:
                    first = pre
                    second = node
            
            pre = node
            node = node.right
        #print first.val, second.val    
        #print first.val, second.val    
        first.val, second.val = second.val, first.val
        
        
