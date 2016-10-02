"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
"""

"""
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0]*(rowIndex+1)
        result[0]=1
        for i in range(1,rowIndex+1):
            for j in range(i, 0, -1):
                result[j] = result[j]  +result[j-1]
        return result
        
