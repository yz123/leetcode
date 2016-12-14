"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

"""

#https://leetcode.com/articles/range-sum-query-mutable/
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.n = len(nums)
        self.tree = [0]* (2*self.n)
        
        #build trees
        for i, j in zip( xrange(self.n, 2*self.n), xrange(self.n)):
            self.tree[i] = nums[j]
        
        for i in xrange(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        pos = self.n + i
        self.tree[pos] =val
        while pos> 0:
            left = pos
            right = pos
            if pos %2 ==0:#pos is on the left side
                right = pos + 1
            else:
                left = pos -1
            self.tree[pos/2] = self.tree[left] + self.tree[right]
            pos /= 2
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        l = i + self.n
        r = j + self.n
        
        sum = 0
        while l<=r:
            if l%2 == 1:
                sum += self.tree[l]
                l = l + 1
            if r %2 == 0:
                sum += self.tree[r]
                r = r -1
            l /= 2
            r /= 2
        return sum
        
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
