"""
There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color 0;
costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?
"""

#dp(n, k) n houses, k colors
#dp(i,j) = cost(i, j) + min( dp(i-1, l)  where l!=k)
#dp(0, j) = cost(i, j)

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        dp = [ [ 0 for j in xrange(k) ] for i in xrange(n) ]

        #dp[0][j]
        for j in xrange(k):
            dp[0][j] = costs[0][j]

        for i in xrange(1, n):
            for j in xrange(k):
                min_pre = dp[i-1][(j+1)%k]
                for m in xrange(k):
                    if m!=j and dp[i-1][m]<min_pre:
                        min_pre = dp[i-1][m]
                dp[i][j] = costs[i][j] + min_pre
        return min(dp[-1])

a = Solution()
costs=[ [3, 2, 1], [1, 2,3], [2, 3, 2] ]
print a.minCostII(costs)
