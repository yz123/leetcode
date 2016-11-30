"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        path = []
        cur = 0
        candidates.sort()
        self.recursion(candidates, path, cur, target)
        return self.res
    
    def recursion(self, candidates, path, cur, target):
        
        for i in xrange(len(candidates)):
            num = candidates[i]
            if cur + num == target:
                self.res.append(path+[num])
            elif cur + num < target:
                path.append(num)
                self.recursion(candidates[i:], path, cur+num, target)
                path.pop()
        
