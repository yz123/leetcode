"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #http://www.cnblogs.com/AnnieKim/archive/2013/04/21/3034631.html
        #虽然不能再另外开辟非常数级的额外空间，但是可以在输入数组上就地进行swap操作。
        #思路：交换数组元素，使得数组中第i位存放数值(i+1)。最后遍历数组，寻找第一个不符合此要求的元素，返回其下标。整个过程需要遍历两次数组，复杂度为O(n)。
        
        i = 0
        n = len(nums)
        while i<n:
            if nums[i]>0 and nums[i]<=n and nums[i]!=i+1 and nums[i]!=nums[ nums[i]-1 ] :
                tmp = nums[ nums[i]-1 ]
                nums[ nums[i]-1 ] = nums[i]
                nums[i] = tmp
                #nums[i], nums[ nums[i]-1 ] = nums[ nums[i]-1 ], nums[i]
            else:
                i += 1
        
        for i in xrange(len(nums)):
            if nums[i]!=i+1:
                return i+1
        
        return n+1
        
