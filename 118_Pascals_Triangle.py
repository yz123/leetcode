"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
#http://blog.csdn.net/DERRANTCM/article/details/47588929
"""
对任意的n>0有 
　　f(1, n)=1，(n>0) 
　　f(1, 2)=1，(n=2) 
　　f(i,j) = f(i-1, j-1)+f(i, j-1)，i>2,j>2 
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tri =[]
        for i in range(numRows):
            if i == 0:
                tri.append([1])
            elif i == 1:
                tri.append([1,1])
            else:
                pre = tri[i-1]
                new = [1]
                for j in range(i-1):
                    new.append(pre[j]+pre[j+1])
                new.append(1)
                tri.append(new)
        return tri
