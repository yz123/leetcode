"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.find_leftmost(nums, 0, len(nums)-1, target)
        if left == -1: 
            return [-1,-1]
        else:
            right = self.find_rightmost(nums, left, len(nums)-1, target)
            return [left, right]
            
    
    def find_leftmost(self, nums, begin, end, target):
        while begin<=end:
            mid = begin + (end-begin)/2
            if nums[mid] == target:
                if (mid ==0 or nums[mid-1]!=target):
                    return mid
                else:
                    end = mid-1
            elif nums[mid]> target:
                end = mid-1
            else:
                begin = mid+1
        
        return -1
    
        
    def find_rightmost(self, nums, begin, end, target):
        while begin<=end:
            mid = begin + (end-begin)/2
            if nums[mid] == target:
                if (mid ==len(nums)-1 or nums[mid+1]!=target):
                    return mid
                else:
                    begin = mid + 1
            elif nums[mid]> target:
                end = mid-1
            else:
                begin = mid+1
        
        return -1
