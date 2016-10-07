"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Subscribe to see which companies asked this question
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#BST[3] = BST[0]*BST[2] + BST[1]*BST[1] + BST[2]*BST[0]
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #return self.dynamicprogramming(n)
        if n>0:
            return self.divid_and_conquer(1, n)
        else:
            return []
    
    #n的子树，root的值跟n相差diff  
    def divid_and_conquer(self, start, end):
        
        if start > end: return [None]
        res = []
        for i in range(start, end+1):
            left_list = self.divid_and_conquer(start, i-1)
            right_list = self.divid_and_conquer(i+1, end)
            for lt in left_list:
                for rt in right_list:
                    root = TreeNode(i)
                    root.left = lt
                    root.right = rt
                    res.append(root)
        return res
        
    def dynamicprogramming(self, n):
        dp = [ [] for i in range(n+1)]
        dp[0]=[None]
        for i in range(1,n+1):
            for left in range(i):
                right = i-1-left
                ltrees = dp[left]
                rtrees = dp[right]
                for lt in ltrees:
                    for rt in rtrees:
                        #print i
                        root = TreeNode(left+1)
                        root.left = self.get_trees(lt, 0)
                        root.right = self.get_trees(rt, left+1)
                        dp[i].append(root)
        dp[0]=[]            
        return dp[n]
    
    def get_trees(self, tree, add_value):
        if not tree: return None
        new_tree = TreeNode(tree.val+add_value)
        new_tree.left = self.get_trees(tree.left, add_value)
        new_tree.right = self.get_trees(tree.right, add_value)
        
        return new_tree
