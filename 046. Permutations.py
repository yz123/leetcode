"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.bfs(nums)
        
        index = 0
        self.result = []
        cur = []
        self.recursion(nums, [])
        return self.result

    def recursion(self, nums, cur_list):
        if len(nums) == 1:
            self.result.append(cur_list+nums)
        for i in xrange(len(nums)):
            cur_list.append(nums[i])
            new_nums = nums[:i]+nums[i+1:]
            self.recursion(new_nums, cur_list)
            cur_list.pop()
            
    def bfs(self, nums):
        q = []
        q.append( ([], nums) )
        for j in xrange(len(nums)):
            tmp = []
            for item in q:
                (cur_list, rest_list) = item
                for i in xrange(len(rest_list)):
                    tmp.append( (cur_list+[rest_list[i]], rest_list[:i]+rest_list[i+1:]) )
            q = tmp
        res = []
        for item in q:
            res.append(item[0])
        return res
        
