"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Idea:
1) Calculate the medians m1 and m2 of the input arrays ar1[] and ar2[] respectively.
2) If m1 and m2 both are equal then we are done, and return m1 (or m2)
3) If m1 is greater than m2, then median is present in one of the below two subarrays.
  a) From first element of ar1 to m1 (ar1[0...|_n/2_|])
  b) From m2 to last element of ar2 (ar2[|_n/2_|...n-1])
4) If m2 is greater than m1, then median is present in one of the below two subarrays.
  a) From m1 to last element of ar1 (ar1[|_n/2_|...n-1])
  b) From first element of ar2 to m2 (ar2[0...|_n/2_|])
5) Repeat the above process until size of both the subarrays becomes 2.
6) If size of the two arrays is 2 then use below formula to get the median.
Median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
"""

#recursion function
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        
        #odd
        if (m+n)%2!=0:
            return self.findKth(nums1, nums2, (m+n)/2, 0, m-1, 0, n-1)*1.0
        #even
        else:
            return ( self.findKth(nums1, nums2, (m+n)/2, 0, m-1, 0, n-1) + self.findKth(nums1, nums2, (m+n)//2-1, 0, m-1, 0, n-1) ) * 0.5
        
  
    def findKth(self, A, B, k, a_begin, a_end, b_begin, b_end):
        while True:      
          len_a = a_end - a_begin + 1
          len_b = b_end - b_begin + 1
          #print A, B
          #print k, a_begin, a_end, b_begin, b_end
          if len_a ==0:
              return B[b_begin+k]
          if len_b ==0:
              return A[a_begin+k]
          if k == 0:
              return min(A[a_begin], B[b_begin])
            
          piv_a = k* len_a /(len_a + len_b)
          #piv_b = k* len_b / (len_a + len_b)
          piv_b =k-piv_a-1
          
          index_a = a_begin + piv_a
          index_b = b_begin + piv_b
          if A[index_a] > B[index_b]:
              k = k- (index_b - b_begin +1)
              a_end = index_a
              b_begin = index_b + 1
              
          else:
              k = k- (index_a - a_begin  +1)
              a_begin = index_a +1
              b_end = index_b
    
        
def main():
    A = [1,2]
    B = [1,1,3]
    #print A
    qs = Solution()
    print qs.findMedianSortedArrays(A,B)

if __name__=="__main__":
    main()
