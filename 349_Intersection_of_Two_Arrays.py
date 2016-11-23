"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""
class Solution(object):
    
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #return list(set(nums1)&set(nums2))
        
        intersec={}
        for n in nums1:
            intersec[n]=1
        inter=[]
        for n in nums2:
            if ( n in intersec ) and intersec[n]>0 :
                intersec[n]-=1
                inter.append(n)
        return inter
    
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(self.get_intersection(nums1, nums2))
        
        return list(set(nums1) & set(nums2))
        
    def get_intersection(self, nums1, nums2):
        hash = {}
        for num in nums1:
            hash[num] = hash.setdefault(num, 0)+1
        
        for num in nums2:
            if num in hash:
                del hash[num]
                yield num
