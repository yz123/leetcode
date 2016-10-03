"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #self.bfs(root)
        #self.dfs(root)
        self.iterative(root)
    
    def iterative(self, root):
        if not root:
            return 
        node = root
        while node.left:
            this = node
            while this:
                this.left.next = this.right
                if this.next:
                    this.right.next = this.next.left
                this = this.next
            node = node.left
            
    def dfs(self, root):
        if (not root) or (root.left == None and root.right == None):
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.dfs(root.left)    
        self.dfs(root.right)
        
        
    
    def bfs(self, root):
        if not root:
            return
        q = []
        q.append(root)
        while len(q)!=0:
            tmp = []
            for i in range(len(q)-1):
                q[i].next = q[i+1]
                if q[i].left:
                    tmp.append(q[i].left)
                if  q[i].right:
                    tmp.append(q[i].right)
            q[-1].next = None
            if  q[-1].left:
                tmp.append(q[-1].left)
            if  q[-1].right:
                tmp.append(q[-1].right)
            q=tmp
