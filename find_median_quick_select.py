"""
Given array A of size n and integer k,
find the k-th elements in A
for example: A = [4,2,1,3,5], k=3
return 3

Idea:
QuickSelect: Given array A of size n and integer k · n,
1. Pick a pivot element p at random from A.
2. Split A into subarrays LESS and GREATER by comparing each element to p as in Quicksort. While we are at it, count the number L of elements going in to LESS.
3. (a) If L = k − 1, then output p.
   (b) If L > k − 1, output QuickSelect(LESS, k).
  (c) If L < k − 1, output QuickSelect(GREATER, k − L − 1)
  
Time Complexity: avarage
T(n) < 4n 
T(n) <= (n-1) + 2/n \sum_{i=n/2}^(n-1) T(i) 
Induction: T(i)<=4i
"""
import random

class Solution(object):
	def quickSelection(self, A, k):
		sel = random.choice(A)
		Great = []
		Small = []
		
		for ele in A:
			if sel > ele:
				Small.append(ele)
			elif sel < ele:
				Great.append(ele)
		
		L = len(Small)
		if L == k-1:
			return sel
		elif L > k-1:
			return self.quickSelection(Small, k)
		else:
			return self.quickSelection(Great, k-L-1)

def main():
	A = [2,3,4,5,6,7]
	qs = Solution()
	print qs.quickSelection(A,5)

if __name__=="__main__":
	main()
