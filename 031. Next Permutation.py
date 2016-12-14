"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # 1 5 8 4 6 6 5 3 1
        # 1 5 8 5 | 6 6 4 3 1
        # 1 5 8 5 | 1 3 4 6 6
        if len(nums) >1:
            i = len(nums) - 2
            while i>=0 and nums[i] >= nums[i+1]:
                i -= 1
            if i >=0:
                j = len(nums) - 1
                while nums[j] <= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
        
                nums[i+1: len(nums)] = nums[ len(nums)-1:i : -1]
            
            if i == -1:
                #nums = nums[::-1]
                nums.sort()
            #print i, nums
