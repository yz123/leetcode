"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.short_code(nums, target)
        return self.binary_search(nums, target)
    
    def short_code(self, nums, target):
        if not nums: return 0
        begin, end = 0, len(nums)-1
        while begin <= end:
            middle = begin + (end - begin)/2
            if nums[middle] == target: 
                return middle
            elif nums[middle] < target:
                begin = middle + 1
            else:
                end = middle -1
        return begin
    
    def binary_search(self, nums, target):
        if not nums: return 0
        begin, end = 0, len(nums)-1
        
        while begin <= end:
            middle = begin + (end - begin)/2
            if nums[middle] == target: 
                return middle
            
            elif nums[middle] < target:
                if middle< end and target < nums[middle+1]:
                    return middle+1
                else:
                    begin = middle + 1
                
            else: #nums[middle] > target:
                if middle > begin and target > nums[middle-1]:
                    return middle 
                else:
                    end = middle -1
        return begin
