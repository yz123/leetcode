"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        a= sum(set(nums))*3 - sum(nums)
        return a/2
        """
        
        """
        http://bangbingsyb.blogspot.com/2014/11/leetcode-single-number-i-ii.html
        http://www.jiuzhang.com/solutions/single-number-ii/
        """
        # d is used to store the sum of each bit
        
        """
        d = [ 0 for i in range(32) ]
        for num in nums:
            for i in range(32):
                mask = (1<<i)
                bit = mask & num
                if bit > 0:
                    d[i] += 1
        
        # get the number that happens once
        # idea: for each bit in d, d[i], d[i] % 3 is the bit
        result = 0
        for i in range(32):
            bit = d[i] %3
            if bit == 1:
                result += ( bit << i)
            
        return result
        """
        
        #from low to high bit
        result = 0
        for i in range(32):
            bitsum = 0
            mask = (1<<i)
            for num in nums:
                if mask & num:
                    bitsum+=1
            bit = bitsum%3
            result = result+ (bit << i)
        return result
        
        """
        #from high to low bit
        result = 0
        for i in range(31, -1,-1):
            bitsum = 0
            mask = (1<<i)
            for num in nums:
                if (mask & num):
                    bitsum +=1
                #bitsum += (mask & num)
            
            result = (result << 1) + ( bitsum%3 ) 
        return result    
        """
        
        """
        one = 0
        second = 0
        for num in nums:
            one = (one ^ num) & ~second
            second = (second ^ num) & ~one
            
        return one
        """
