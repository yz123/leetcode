"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list = []
        stack = []
        #stack: (node, tag); tag == 0: 第一次入栈； tag == 1:第二次入栈
        if root!=None:
            node = root
            mask = 0
            while True:
                while node:
                    stack.append( (node,0))
                    node = node.left
                
                (node, tag) = stack.pop()
                #print node.val, tag
                while tag == 1 :
                    list.append(node.val)
                    if len(stack)!=0:
                        (node, tag) = stack.pop()
                    else:
                        mask =1
                        break
                if mask ==1:
                    break
                stack.append((node, 1))
                node = node.right
                
        return list
     
    """ 
    #recursion    
    def postorderTraversal(self, root):
        list = []
        if root!=None:
            ll = self.postorderTraversal(root.left)
            rl = self.postorderTraversal(root.right)
            list += ll
            list += rl
            list.append(root.val)
        return list
    """
