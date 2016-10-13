"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        """
        return self.iterative(nums)
        """
        return self.bfs(nums)
        
        """
        if len(nums)==0: return [ ]
        self.res =[]
        nums=sorted(nums)
        self.res.append([])
        self.dfs(nums, [], 0)
        return self.res
        """
        
        
    
    def bfs(self, nums):
        if len(nums)==0: return [ ]
        
        nums= sorted(nums)
        length = len(nums)
        q = []
        res = []
        nextindex = 0 #next index
        q.append( ([], nextindex))
        res.append([])
        while q:
            nextLevel = []
            for i in xrange(len(q)):
                (above_list, nextindex) = q[i]
                if nextindex<=length-1:
                    for j in xrange(nextindex, length):
                        if j!=nextindex and nums[j]==nums[j-1]:
                            continue
                        newset = above_list +[nums[j]]
                        res.append(newset)
                        nextLevel.append(  (newset, j+1) )
            q= nextLevel
            nextLevel = []
            
        return res
    
    def dfs(self, nums, curset, nextlevel):
        
        length = len(nums)
        if nextlevel <=length-1:
            for i in xrange(nextlevel, length):
                if i!=nextlevel and nums[i] == nums[i-1]:
                    continue
                nextset = curset +[nums[i]]
                self.res.append(nextset)
                self.dfs(nums, nextset, i+1)
        
    #when add new element in the result, the result expands 2 time. For example: [[], [1]] --> expand 2, [ [], [1] ]+ [ []+[2],[1]+[2]  ]    
    def iterative(self, nums):
        res = []
        res.append( [] )
        nums=sorted(nums)
        for num in nums:
            tmp = list(res)
            for l in tmp:
                next = l+[num]
                if next not in res:
                    res.append( l+[num])
        return res
