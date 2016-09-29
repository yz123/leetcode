"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""
#idea: DP. keep curmax, curmin

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cp = nums[0]
        curmax = nums[0]
        curmin = nums[0]
        for i in range(1, len(nums)):
            tmp = max( curmax*nums[i], curmin*nums[i], nums[i] )
            if tmp > cp:
                cp = tmp
            
            curmin = min( curmax*nums[i], nums[i], curmin*nums[i])
            curmax = tmp
        return cp
