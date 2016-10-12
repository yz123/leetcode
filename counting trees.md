http://stackoverflow.com/questions/3042412/with-n-no-of-nodes-how-many-different-binary-and-binary-search-trees-possib

http://www-math.mit.edu/~djk/18.310/18.310F04/counting_trees.html

This suggests the hypothesis: F(n) = n^n-2.

Total no of Binary Trees are = enter image description![enter image description here
Summing over i gives the total number of binary search trees with n nodes. enter image description here
The base case is t(0) = 1 and t(1) = 1, i.e. there is one empty BST and there is one BST with one node. enter image description here

So, In general you can compute total no of Binary Search Trees using above formula. I was asked a question in Google interview related on this formula. Question was how many total no of Binary Search Trees are possible with 6 vertices. So Answer is t(6) = 132



