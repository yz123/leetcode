"""
Given array A of size n and integer k,
find the k-th elements in A
for example: A = [4,2,1,3,5], k=3
return 3

Idea:
DeterministicSelect: Given array A of size n and integer k,
1. Group the array into n/5 groups of size 5 and find the median of each group. (For simplicity, we will ignore integrality issues.)
2. Recursively, find the true median of the medians. Call this p.
3. Use p as a pivot to split the array into subarrays LESS and GREATER.
4. Recurse on the appropriate piece.
"""
class Solution(object):
	def deterministicSelection(self, A, k):
		sel = self.get_median_of_median(A)
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
			return self.deterministicSelection(Small, k)
		else:
			return self.deterministicSelection(Great, k-L-1)
			
	def get_median_of_median(self, A):
		n = len(A)
		medians = []
		i=0
		temp=[]
		for ele in A:
			temp.append(ele)
			i+=1
			if i==5:
				temp.sort()
				medians.append(temp[2])
				i=0
		if i!=5:
			temp.sort()
			medians.append(temp[len(temp)/2])
			temp=[]
		medians.sort()
		return medians[len(medians)/2]

def main():
	A = [2,3,4,5,6,7]
	qs = Solution()
	print qs.deterministicSelection(A,3)

if __name__=="__main__":
	main()
