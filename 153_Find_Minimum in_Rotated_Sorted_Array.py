"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

#idea: if middle < end: left side; middle>end : right side 
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin, end = 0, len(nums)-1
        while begin < end:
            middle = begin + ( end - begin )/2
            mnum = nums[middle]
            if mnum > nums[end]:
                begin = middle + 1
            else:
                end = middle
        return nums[begin]
    
   
            
    """
    #recursion
    def findMin(self, nums):
        begin, end = 0, len(nums)-1
        return self.binsearch(nums, begin, end)
    
    def binsearch(self, nums, begin, end):    
        if begin < end:
            middle =begin +  ( end - begin )/2
            mnum = nums[middle]
            if mnum > nums[end]:
                return self.binsearch(nums, middle+1, end)
            else:
                return self.binsearch(nums, begin, middle)
        else:
            return nums[begin]
    """
