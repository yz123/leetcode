"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.divide_and_conquer(nums, 0, len(nums)-1)
        return self.dp(nums)
    
    #idea: 到i为止最大的元素: dp[i] = max( dp[i-1]+nums[i], nums[i])
    def dp(self, nums):
        
        dp = nums[0]
        max_sum = dp
        for i in xrange(1, len(nums)):
            dp = max(dp+nums[i], nums[i])
            max_sum = max(max_sum, dp)
            
        return max_sum
        
        #with array
        dp = [0]*len(nums)
        dp[0]=nums[0]
        max_sum = dp[0] 
        
        for i in xrange(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
            
        return max_sum
        
    def divide_and_conquer(self, nums, begin, end):
        if begin >=end:
            return nums[begin]
        
        mid = begin+ (end-begin)/2
        
        l = self.divide_and_conquer(nums, begin, mid-1)
        r = self.divide_and_conquer(nums, mid+1, end)
        
        max_l = nums[mid]
        sum = 0
        for i in xrange(mid, begin-1, -1):
            sum += nums[i]
            if sum>max_l:
                max_l = sum
            
        
        max_r = nums[mid]
        sum = 0
        for i in xrange(mid, end+1):
            sum +=nums[i]
            if sum>max_r:
                max_r = sum
        
        m = max_l + max_r -nums[mid]
        #print nums[mid], l, r, m, max_l, max_r
        return max(l, r, m)
