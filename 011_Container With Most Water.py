class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.dp(height)
        
    #https://discuss.leetcode.com/topic/50763/from-dp-to-greedy-o-n-with-explanation-easy-way-to-see-this-problem
    #dp[i,j]: max container from i to j
    #dp[i, j] = max(area(i,j), dp[i+1,j], dp[i,j-1])
    #dp[0, n] = max of : (1) area(0,n); (2) if h[0]>=h[n]: dp[0, n-1]; (3) if h[0]<h[n]: dp[1, n-1]
    
    def dp(self, height):
        if not height: return 0
        
        max_c = 0
        n = len(height)-1
        i,j = 0, n
        while i<j:
            area = (j-i) * min( height[i], height[j])
            max_c = max(max_c, area)
            if height[i] >= height[j]:
                j -= 1
            else: #height[i] < height[j]
                i += 1
                
        return max_c
