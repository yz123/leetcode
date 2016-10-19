"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        #bit opreation
        return self.bit_operation(nums)
        
        #backtracking bfs
        return self.backtracking_bfs(nums)
        
        #backtracking dfs
        self.res = []
        self.res.append([])
        self.backtracking(nums, 0, [])
        return self.res
        
    #general a bit, for example, n=2, 00, 01, 10, 11, check who to choose
    def bit_operation(self, nums):
        length = len(nums)
        n_sets = 1 << length
        
        res = []
        for i in xrange(n_sets):
            ans = []
            for bit in xrange(length):
                check = (1<< bit)
                if ( check & i ) == check: #if  ((1<<bit) & i )== (1<<bit):
                #if ( (i >> bit) & 1 ) == 1:    
                    ans.append(nums[bit] )
            res.append(ans)
        
        return res
    
    #idea: build a search tree, then dfs
    def backtracking(self, nums, begin_index, pre_sol):
        
        for i in xrange(begin_index, len(nums)):
            cur_sol = pre_sol + [nums[i]]
            self.res.append(cur_sol)
            self.backtracking(nums, i+1, cur_sol)
    
    #idea: build a search tree, then bfs            
    def backtracking_bfs(self, nums):
        
        q = []
        next_index = 0
        res = []
        res.append([])
        q.append( ([], 0))
        
        while q:
            (pre, next_index)= q.pop(0)
            for i in xrange(next_index, len(nums)):
                cur = pre + [nums[i]]
                q.append( (cur, i+1)  )
                res.append(cur)
        return res
        
