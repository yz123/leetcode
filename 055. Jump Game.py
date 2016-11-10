"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.forwardcheck(nums)
        
        return self.backcheck(nums)
        
    def forwardcheck(self, nums):
        rightmost = 0
        for i in xrange(len(nums)):
            #cannot pass the rightmost
            if i>rightmost:
                return False
            if i + nums[i]>rightmost:
                rightmost = i + nums[i]
            
            if rightmost >= len(nums)-1:
                return True
        return False
        
    """
    idea: Think it backwards from right to left. If {x1, x2, x3} can all reach the last one, which one will you pick? It doesn't matter since there must be a path to any one of them, if there is a global path from 0 to n-1. So f(0, n-1) is equal to f(0, xi), where f(a, b) means there is a path from a to b. So what we need to do is to scan backwards and check if all intermediate stones we select can be reached.
    """
    def backcheck(self, nums):
        
        trace_back = len(nums)-1
        
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i]+i >= trace_back:
                trace_back = i
        return trace_back==0
