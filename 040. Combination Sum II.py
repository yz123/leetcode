"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        cur_index = 0
        path = []
        cur_sum = 0
        candidates.sort()
        self.recursion(candidates, cur_index, path, cur_sum, target)
        
        return self.res
    
    def recursion(self, candidates, cur_index, path, cur_sum, target):
        for i in xrange(cur_index, len(candidates)):
            if i>cur_index and candidates[i]== candidates[i-1]:
                continue
            num = candidates[i]
            if cur_sum + num == target:
                self.res.append(path+[num])
            elif cur_sum + num < target:
                path.append(num)
                self.recursion(candidates, i+1, path, cur_sum+num, target)
                path.pop()
