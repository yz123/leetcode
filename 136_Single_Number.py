"""
136 Signle Numbers
Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
p XOR q = ( p | q ) & ~( p & q)
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         return sum(list(set(nums)))*2 - sum(nums)
        """
        
        return reduce(lambda x, y: x^ y, nums)
        
        '''
        single_number = nums[0]
        for i in range(1, len(nums)):
            single_number = single_number ^ nums[i]
        return single_number
        '''
        
        '''
        return sum(list(set(nums)))*2 - sum(nums)
        '''


""" Submission Detail
15 / 15 test cases passed.
Status: Accepted
Runtime: 52 ms
Submitted: 0 minutes ago
"""
