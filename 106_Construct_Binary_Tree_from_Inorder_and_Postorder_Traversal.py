"""
Given inorder and postorder traversal of a tree, construct the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.iterative1(inorder, postorder)
        #return self.iterative(inorder, postorder)
        
        #recursive version
        """
        self.d = {}
        for i in range(len(inorder)):
            self.d[ inorder[i] ] = i
        return self.dfs_recursion(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)
        """
    
    
    def iterative1(self, inorder, postorder):
        if len(inorder) ==0: return None
        stack = []
        root = TreeNode( postorder[-1] )
        stack.append(root)
        node = root
        #i: index of inorder
        i = len(inorder)-1
        p = len(postorder)-2
        
        while True:
            if stack[-1].val == inorder[i]:
                node=stack.pop()
                i = i-1
                if i<0:
                    break
                if stack and stack[-1].val == inorder[i]:
                    continue
                node.left = TreeNode(postorder[p])
                p = p-1
                node = node.left
                stack.append(node)
            else:
                node.right = TreeNode(postorder[p])
                p = p-1
                node = node.right
                stack.append(node)
        return root
                
                
    #https://discuss.leetcode.com/topic/54223/annotated-iterative-solution-with-comments-does-not-modify-parameters
    #http://www.cnblogs.com/jdneo/p/5154984.html
    #https://discuss.leetcode.com/topic/10244/my-o-n-19ms-solution-without-recusion-hope-help-you
    #中序: 3 2 4 1 6 5 7
    #后序：3 4 2 6 7 5 1
    #idea：从后序向前，如果不等于中序， 说明右子树还没有遍历完，遍历右子树，如果等于，则转向左子树 
    def iterative(self, inorder, postorder):
        if len(inorder)==0: return None
        
        root = TreeNode( postorder[-1] )
        stack = []
        stack.append(root)
        node = root
        #i: index of inorder
        i = len(inorder)-1
        for p in range(len(postorder)-1, -1, -1):
            if postorder[p]!=inorder[i]:
                node.right = TreeNode( postorder[p-1])
                node = node.right
                stack.append(node)
            else:
                while len(stack)!=0 and stack[-1].val == inorder[i]:
                    node = stack.pop()
                    i = i -1
                #print p, i
                if p > 0 :
                    node.left = TreeNode( postorder[p-1])
                    node = node.left
                    stack.append(node)
        return root
    
    def dfs_recursion(self, inorder, postorder, ibegin, iend, pbegin, pend):
        if ibegin > iend: return None
        
        root = TreeNode( postorder[ pend ] )
        index = self.d[ root.val ]
        root.left = self.dfs_recursion(inorder, postorder, ibegin, index-1, pbegin, pbegin + (index-ibegin)-1 )
        root.right = self.dfs_recursion(inorder, postorder, index+1, iend, pbegin + (index-ibegin) , pend-1 )
        return root
        
