"""
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red;
costs[1][2] is the cost of painting house 1 with color green,
and so on... Find the minimum cost to paint all houses.
"""

#idea
#red, blue, green[i] = cost[i]+min( othercolor[i-1])
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        n= len(costs)
        red = [ 0 for i in xrange(n)]
        blue = [ 0 for i in xrange(n)]
        green = [ 0 for i in xrange(n)]

        red[0], blue[0], green[0] = costs[0][0], costs[0][1], costs[0][2]
        for i in xrange(1, n):
            red[i] = costs[i][0] + min( blue[i-1], green[i-1])
            blue[i] = costs[i][0] + min(red[i - 1], green[i - 1])
            green[i] = costs[i][0] + min(blue[i - 1], red[i - 1])
        return min(red[-1], blue[-1], green[-1])

a = Solution()
costs=[ [3, 2, 1], [1, 2,3], [2, 3, 2] ]
print a.minCost(costs)
