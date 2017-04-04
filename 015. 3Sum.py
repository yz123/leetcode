"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.sum(nums)
        return self.two_sum(nums)
    
    def sum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
    
    def two_sum(self, nums):
        nums = sorted(nums)
        res = []
        for i, n in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue
            nums1 = nums[i+1:]
            target = -n
            dict = {}
            for i, num in enumerate(nums1):
                if target - num in dict:
                    res.append( [n, num, target-num])
                else:
                    dict[num] = i
        return res 
