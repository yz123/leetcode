"""136 Signle Numbers
Given an array of integers, every element appears twice except for one. Find that single one.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single_number = nums[0]
        for i in range(1, len(nums)):
            single_number = single_number ^ nums[i]
        return single_number


""" Submission Detail
15 / 15 test cases passed.
Status: Accepted
Runtime: 52 ms
Submitted: 0 minutes ago
"""
