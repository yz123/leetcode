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
