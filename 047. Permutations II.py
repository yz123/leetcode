"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.bfs(nums)
        
        nums = sorted(nums)
        self.res = []
        self.recursion([], nums)
        return self.res
    
    def recursion(self, cur_path, nums):
        if len(nums)==1:
            self.res.append(cur_path+nums)
        
        else:
            for i in xrange(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                cur_path.append(nums[i])
                self.recursion( cur_path, nums[:i]+nums[i+1:] )
                cur_path.pop()
    
    def bfs(self, nums):
        nums = sorted(nums)
        q = []
        q.append( ([], nums) )
        for j in xrange(len(nums)):
            tmp = []
            for item in q:
                (cur_list, rest_list) = item
                for i in xrange(len(rest_list)):
                    if i>0 and rest_list[i-1] == rest_list[i]:
                        continue
                    tmp.append( (cur_list+[rest_list[i]], rest_list[:i]+rest_list[i+1:]) )
            q = tmp
        res = []
        for item in q:
            res.append(item[0])
        return res
