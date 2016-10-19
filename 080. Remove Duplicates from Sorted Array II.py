"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3: return len(nums)
        
        cur = 1
        for j in xrange(2, len(nums)):
            if nums[j]!= nums[cur-1]:
                cur = cur + 1
                nums[cur] = nums[j]
        
        return cur + 1
