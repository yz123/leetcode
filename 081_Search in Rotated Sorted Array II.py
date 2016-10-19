"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        begin, end = 0, len(nums)-1
        while begin <= end:
            middle = begin + (end - begin )/2
            m = nums[middle]
            if m == target:
                return True
            else: # m!=target
            
                if m > nums[end]:
                    if target < m and target >= nums[begin]:
                        end = middle - 1
                    else:
                        begin = middle + 1
                        
                elif m < nums[end]:
                    if target > m and target <= nums[end]:
                        begin = middle + 1
                    else:
                        end = middle - 1
                   
                else: #m = nums[end]
                    if m != nums[begin]:
                        end = middle -1
                    else: #m = nums[begin]=nums[end]
                        begin = begin + 1
                        end = end -1
                        
        return False
        
