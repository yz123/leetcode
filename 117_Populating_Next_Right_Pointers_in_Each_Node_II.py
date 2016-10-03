"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
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
    
    #把下一层想做linkedlist, 用一个dummy为head头
    def iterative(self, root):
        if not root:
            return
        head = root
        while head:
            cur = head
            
            #set the next head to be None
            head = None
            
            #the start of the next layer
            dummy = TreeLinkNode(0)
            #link the next layer
            while cur:
                #get left and right linked
                if cur.left:
                    if not head:
                        head = cur.left
                    dummy.next = cur.left
                    dummy = dummy.next
                if cur.right:
                    if not head:
                        head =cur.right
                    dummy.next =cur.right
                    dummy = dummy.next
                cur = cur.next
            
        
        
    def dfs(self, root):
        if (not root) or (root.left==None and root.right==None):
            return
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                nei = root.next
                while nei:
                    if nei.left:
                        root.left.next = nei.left
                        break
                    if nei.right:
                        root.left.next = nei.right
                        break
                    nei=nei.next
        if root.right:
            nei = root.next
            while nei:
                if nei.left:
                    root.right.next = nei.left
                    break
                if nei.right:
                    root.right.next = nei.right
                    break
                nei=nei.next
        
        #must start with root.right (必须把右边处理完)
        self.dfs(root.right)            
        self.dfs(root.left)    
        
        
        
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
