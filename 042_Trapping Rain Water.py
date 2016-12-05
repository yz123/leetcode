"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
"""

#http://bangbingsyb.blogspot.com/2014/11/leetcode-trapping-rain-water.html
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.two_pointer(height)
        return self.dp(height)
        return self.use_stack(height)
    
    #用一个栈存放前面比当前元素小的
    # 扫描数组，如果遇到比zhua
    def use_stack(self, height):
        if len(height)<3: return 0
        stack = []
        stack.append(0)
        
        water = 0
        for i in xrange(1, len(height)):
            #看是否可以注水
            if height[i]> height[ stack[-1] ]:
                bottom = height[ stack.pop() ]
                
                while len(stack)>0  and (height[i]>= height[stack[-1]]):
                    #print height[stack[-1]], bottom
                    water += (height[stack[-1]] - bottom)* (i - stack[-1]-1)
                    bottom = height[stack.pop()]
                if len(stack)>0:
                    water += (height[i] - bottom)* (i - stack[-1]-1)
            stack.append(i)
        return water
    
    #对于每个bar，找到左右最大的高度，然后这个bar的水为min(left, right) -A[i]           
    def dp(self, A):
        if len(A) < 3: return 0
        
        #dp[i] = max(dp[i-1], A[i-1])
        dp = [0]*len(A)
        dp[0] = A[0]
        for i in xrange(1, len(A)):
            dp[i] = max(dp[i-1], A[i-1])
        
        water = 0
        r_max = A[-1]
        for i in xrange(len(A)-2, -1, -1):
            r_max = max(r_max, A[i+1])
            if min(dp[i], r_max) - A[i] > 0:
                water += min(dp[i], r_max) - A[i]
        return water
    
    #用两个指针, 如果一个小，则移动这个，因为
    #Here is my idea: instead of calculating area by height*width, we can think it in a cumulative way. In other words, sum water amount of each bin(width=1).
    #Search from left to right and maintain a max height of left and right separately, which is like a one-side wall of partial container. Fix the higher one and flow water from the lower part. For example, if current height of left is lower, we fill water in the left bin. Until left meets right, we filled the whole container.
    def two_pointer(self, A):
        if len(A)<3: return 0
        left, right = 0, len(A)-1
        maxleft, maxright = 0, 0
        water = 0
        while left <= right:
            if A[left]<=A[right]:
                if A[left] >= maxleft: 
                    maxleft = A[left]
                else:
                    water += maxleft - A[left]
                left += 1
            else:
                if A[right]>= maxright:
                    maxright = A[right]
                else:
                    water += maxright - A[right]
                right -= 1
        return water
