"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin, end = 0, len(nums)-1
        while begin <= end:
            middle = begin + (end - begin)/2
            mnum = nums[middle]
            if mnum == target: 
                return middle
            else:
                if mnum > nums[end]:
                    if target < mnum and target >= nums[begin]:
                        end = middle -1
                    else:
                        begin = middle +1
                    
                else: # mnum < nums[end]
                    if target > mnum and target <= nums[end]:
                        begin = middle +1
                    else:
                        end = middle -1
        
        return -1
