"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        #return self.inorder_traverse(preorder, inorder)
        return self.inorder_traverse1(preorder, inorder)
        
        """
        #dfs recursion
        self.dic_inorder = {}
        for i in range(len(inorder)):
            self.dic_inorder[inorder[i]] = i
        return self.dfs(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
        """
    
    def dfs(self, preorder, inorder, pi, pj, ii, ij):
        if pi > pj: return None
        root = TreeNode(preorder[pi])
        index = self.dic_inorder[root.val]
        root.left = self.dfs(preorder, inorder, pi+1, pi+index-ii, ii, index-1)
        root.right = self.dfs(preorder, inorder, pi+index-ii+1, pj, index+1, ij)
        return root
    
    #myself
    #https://discuss.leetcode.com/topic/795/the-iterative-solution-is-easier-than-you-think/5
    def inorder_traverse1(self, preorder, inorder):
        if len(preorder) == 0: return None
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        node = root
        cur_pre = 0
        cur_in = 0
        while cur_pre < len(preorder):
            if preorder[cur_pre] != inorder[cur_in]:
                node.left = TreeNode(preorder[cur_pre+1])
                node = node.left
                stack.append(node)
            else:
                #print stack[-1].val, inorder[cur_in]
                while len(stack)!=0 and stack[-1].val== inorder[cur_in]:
                    node = stack.pop()
                    cur_in += 1
                if cur_pre < len(preorder)-1:
                    node.right = TreeNode(preorder[cur_pre+1])
                    node = node.right
                    stack.append(node)
            cur_pre += 1
            #print cur_pre, cur_in
        return root
    
    #https://discuss.leetcode.com/topic/61931/13ms-c-solution-without-recursion
    #https://discuss.leetcode.com/topic/795/the-iterative-solution-is-easier-than-you-think/4
    def inorder_traverse(self, preorder, inorder):
        if len(preorder) == 0: return None
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        node = root
        #cur_pre = 0
        cur_in = 0
        for cur_pre in range(len(preorder)):
            #print preorder[cur_pre], inorder[cur_in]
            if preorder[cur_pre] != inorder[cur_in]:
                node.left = TreeNode(preorder[cur_pre+1])
                node = node.left
                stack.append(node)
            else:
                #print stack[-1].val ==inorder[cur_in]
                while len(stack)!=0 and stack[-1].val ==inorder[cur_in]:
                    node = stack.pop()
                    cur_in += 1
                if cur_pre < len(preorder)-1:
                    node.right = TreeNode(preorder[cur_pre+1])
                    node = node.right
                    stack.append(node)
        return root
