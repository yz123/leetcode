#http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
#http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
#idea:
"""
如果当前节点左孩子为空，则遍历，否则把当前节点移到其左孩子右子树的最后
"""

void inorderMorrisTraversal(TreeNode *root) {
    TreeNode *cur = root, *prev = NULL;
    while (cur != NULL)
    {
        if (cur->left == NULL)          // 1.
        {
            printf("%d ", cur->val);
            cur = cur->right;
        }
        else
        {
            // find predecessor
            prev = cur->left;
            while (prev->right != NULL && prev->right != cur)
                prev = prev->right;

            if (prev->right == NULL)   // 2.a)
            {
                prev->right = cur;
                cur = cur->left;
            }
            else                       // 2.b)
            {
                prev->right = NULL;
                printf("%d ", cur->val);
                cur = cur->right;
            }
        }
    }
}
