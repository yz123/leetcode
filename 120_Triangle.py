"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

#http://blog.csdn.net/nk_test/article/details/49456237
#https://discuss.leetcode.com/topic/19754/python-easy-to-understand-solutions-top-down-bottom-up
#https://discuss.leetcode.com/topic/59473/a-top-bottom-python-solution-with-o-n-space
#triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]) 
class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
                
        return triangle[0][0]    

    """
    #bottom-up
    def minimumTotal(self, triangle):
        if not triangle:
            return
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1])+triangle[i][j]
        return res[0]
    """   
    
    """
    #top-down
    def minimumTotal(self, triangle):
        
        if not triangle: return 0
        dp = [0] * len(triangle)
        temp = []
        for i in range(len(triangle)):
            temp[:] = dp # you can't use temp=dp here
            for j in range(0,i+1):
                # edge cases
                if j == 0:
                    dp[j] = temp[j] + triangle[i][0]
                elif j == i:
                    dp[j] = temp[j-1] + triangle[i][i]
                # else
                else:
                    dp[j] = min(temp[j-1], temp[j]) + triangle[i][j]
        return min(dp)  
    """
