"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

#https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak/31
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.On_method(nums)
        #return self.naive_sorted_way(nums)
    
    #https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak/31
    #check whether a num n is in the dictionary, and if "n" is the start of a sequence, check (how to do: if n-1 not in dic)
    def On_method(self, nums):
        nums = set(nums)
        if nums==None:
            return 0
        longest = 1
        for n in nums:
            if n-1 in nums:
                continue
            m = n
            while m+1 in nums:
                m = m+1
            longest = max(longest, m-n+1)
        return longest
            
                
        
        
    def naive_sorted_way(self, nums):
        nums= list(set(nums))
        a=sorted(nums)
        print a
        max = 0
        cur = 1
        for i in range(1,len(a)):
            if a[i-1]+1 ==a[i]:
                cur+=1
            else:
                if cur>max:
                    max = cur 
                cur = 1
        if cur>max:
            max = cur 
        return max
