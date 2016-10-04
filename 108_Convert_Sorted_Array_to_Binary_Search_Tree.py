"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #return self.bin_search_recursion(nums, 0, len(nums)-1)
        return self.iterative(nums)
    
    def bin_search_recursion(self, nums, begin,end):
        if begin > end:
            return None
        
        middle = begin + (end-begin)/2
        root = TreeNode(nums[middle])
        root.left = self.bin_search(nums,begin, middle-1)
        root.right = self.bin_search(nums,middle+1, end)
            
        return root
    
    #for fun
    def iterative(self, nums):
        length = len(nums)
        if length == 0:
            return None
        
        begin, end = 0, length -1
        stack = []
        root = TreeNode(nums[(end-begin)/2])
        stack.append( (root, begin, end)  )
        while stack:
            (node, begin, end ) = stack.pop()
            middle = begin + (end-begin)/2
            
            #create the right node
            if middle+1 <= end:
                #print middle, end
                node.right = TreeNode(nums[middle+1+ (end- (middle+1))/2])
                stack.append( ( node.right, middle+1, end ) )
                
            #create the left node
            if begin<=middle-1:
                #print begin, middle
                node.left = TreeNode( nums[begin+ (middle -1 -begin)/2] )
                stack.append( (node.left, begin, middle-1)  )
        return root
            
