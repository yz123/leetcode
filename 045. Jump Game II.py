"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.left_to_right(nums)
        
    
    def left_to_right(self, nums):
        #idea
        #用两个指针，左边的往后扫，右边的指向right most
        #当左边指针到达右边是，右边的指针shift到［left, right］中间最右边的位置
        if not nums: return 0
        
        left, right, last = 0, 0, len(nums)-1
        cur_max = 0
        jump = 0
        
        while left<last:
            #left到last右边代表有0出现，不能在前进了
            if left>right:
                return -1
            
            if nums[left]+left > cur_max:
                cur_max = nums[left]+left
            #else: #nums[left]+left < right, do nothing
            
            if left == right:
                right = cur_max
                #print right, nums[right]
                jump += 1
            
            if right>=last:
                break
            
            left +=1
            
        #cannot reach last index
        return jump
