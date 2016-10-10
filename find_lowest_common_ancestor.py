#http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

"""
Method 2 (Using Single Traversal)
The method 1 finds LCA in O(n) time, but requires three tree traversals plus extra spaces for path arrays. If we assume that the keys n1 and n2 are present in Binary Tree, we can find LCA using single traversal of Binary Tree and without extra storage for path arrays.
The idea is to traverse the tree starting from root. If any of the given keys (n1 and n2) matches with root, then root is LCA (assuming that both keys are present). If root doesn’t match with any of the keys, we recur for left and right subtree. The node which has one key present in its left subtree and the other key present in right subtree is the LCA. If both keys lie in left subtree, then left subtree has LCA also, otherwise LCA lies in right subtree.
"""

# Python program to find LCA of n1 and n2 using one
# traversal of Binary tree
 
# A binary tree node
class Node:
     
    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None
     
# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree
def findLCA(root, n1, n2):
     
    # Base Case
    if root is None:
        return None
 
    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root 
 
    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2) 
    right_lca = findLCA(root.right, n1, n2)
 
    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root 
 
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca
 
 
# Driver program to test above function
 
# Let us create a binary tree given in the above example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print "LCA(4,5) = ", findLCA(root, 4, 5).key
print "LCA(4,6) = ", findLCA(root, 4, 6).key
print "LCA(3,4) = ", findLCA(root, 3, 4).key
print "LCA(2,4) = ", findLCA(root, 2, 4).key
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
