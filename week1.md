# 1st Week Report
Yao Zhang


## 1. Two Sum 

```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

### Idea

Use dictionary. 

### Code

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash={}
        i=0
        for n in nums:
            n2 = target - n
            if n2 in hash:
                return [hash[n2], i]
            else:
                hash[n] = i
                i += 1
        return [-1, -1]
```

### Leetcode output
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 48 ms
```

### Reference
None

## 2. Add Two Numbers

```
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
```

### Idea

Use a flag to record whether a new node is needed.

### Code

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l=ListNode(0)
        head = l
        while l1!=None or l2!=None:
            if l1!=None:
                l.val += l1.val
                l1=l1.next
            if l2!=None:
                l.val += l2.val
                l2=l2.next
                
            flag = l.val/10
            if l1!=None or l2!=None or flag!=0:
                l.next =ListNode(l.val/10)
                l.val %= 10
                l=l.next
        
        return head
```

### Leetcode output
```
1556 / 1556 test cases passed.
Status: Accepted
Runtime: 152 ms

```

### Reference
None

## 3. Longest Substring Without Repeating Characters

```
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Idea

Use a dictionary to store whether a character has been repeated. 

And also record the starting point of the current substring. 

If a character has been repeated, it means it is in the dictionary, and previous index >= the starting point of the cur. substring.
Otherwise put the index of the character into the dictionary.

### Code

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        isIn = {}
        start = 0
        length = 0
        for cur in range(len(s)):
            a = s[cur]
            #a is in the substring without repeating characters:
            if ( a not in isIn ) or (isIn[a]<start):
                isIn[a] = cur
                length += 1
            else:
            # a has been repeated:
                if length > longest:
                    longest = length
                start = isIn[a]+1
                isIn[a] = cur
                length = cur - start +1
        if length > longest:
            longest = length
        return longest
```

### Leetcode output
```
982 / 982 test cases passed.
Status: Accepted
Runtime: 100 ms

```

### Reference
None

## 4. Median of Two Sorted Arrays

```
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
```

### Idea

Calculate the medians m1 and m2 of the input arrays ar1[] and ar2[] respectively.

If m1 is greater than m2, then median is present in one of the below two subarrays.
  a) From first element of ar1 to m1 (ar1[0...|_n/2_|])
  b) From m2 to last element of ar2 (ar2[|_n/2_|...n-1])
  
If m2 is greater than m1, then median is present in one of the below two subarrays.
  a) From m1 to last element of ar1 (ar1[|_n/2_|...n-1])
  b) From first element of ar2 to m2 (ar2[0...|_n/2_|])


### Code

```python
#iterative function
# k is the index of the element we want to find
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
```

### Leetcode output
```
2079 / 2079 test cases passed.
Status: Accepted
Runtime: 136 ms

```

### Reference
None

## 5. Longest Palindromic Substring

```
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
```

### Idea

From the current character, check whether its left and right is the same.

### Code

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        start = 0
        end = 0
        for i in range(len(s)):
            l1 = self.getPalindrome(s, i, i)
            l2 = self.getPalindrome(s, i, i+1)
            #print l1, l2
            l = max(l1, l2)
            #print l
            if l> length:
                length =l
                if l %2 ==0:
                    start = i - l/2 +1
                else:
                    start = i -l/2
                end = i+ l/2
            
        return s[start: end+1]
        
    def getPalindrome(self, s, left, right):
        start = 0
        end = len(s) -1
        while left >= start and right <= end and s[left]==s[right]:
            left -=1
            right +=1
        #print left, right
        l = right - left -1    
        return l
```

### Leetcode output
```
88 / 88 test cases passed.
Status: Accepted
Runtime: 1364 ms

```

### Reference
None

## 6. ZigZag Conversion 

```
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
```

### Idea

Use a list to store every line. For each element a, if a% (numRow-1)*2 == k or (numRows -1) - (k -numRows +1), put a into that row

### Code

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        lists=['']*numRows
        N=(numRows-1)*2
        
        for i in range(len(s)):
            if i==0:
                lists[0] += s[i]
            else:
                k = i%N
                index = min(k, (numRows -1) - (k -numRows +1))
                lists[index]+= s[i]
                
        return ''.join(lists)
```

### Leetcode output
```
1158 / 1158 test cases passed.
Status: Accepted
Runtime: 140 ms

```

### Reference
None

## 7. Reverse Integer

```
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
```

### Idea

Use max/ret<10 to decide whether the reverse number will be overflow or not

### Code

```python

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tag = 1
        if x<0:
            x = -x
            tag =0
        
        ret = 0
        max  = 1<<31
        while x>0:
            if ret!=0 and max/ret<10:
                return 0
            ret = ret*10 + x%10
            x /= 10
        
        if tag == 0:
            ret = -ret
        
        return ret

```

### Leetcode output
```
1032 / 1032 test cases passed.
Status: Accepted
Runtime: 60 ms

```

### Reference
None

## 8. 

```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
```

### Idea

1. rest = target - current_value.
2. find rest in a dictionary. 
3. be careful about the same index of rest and current_value. 

### Code

```python
# created by Ji Wang ericshape @ 5/23/16 2:11 PM

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = dict()

        k = 0
        for v in nums:
            sum[v] = k
            k += 1

        k = 0
        for v in nums:
            rest = target - v
            # be careful about the result in same index!
            if rest in sum and k != sum[rest]:
                return [k, sum[rest]]
            k += 1
```

### Leetcode output
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 56 ms
Submitted: 0 minutes ago

```

### Reference
None

## 1. Two Sum 

```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
```

### Idea

1. rest = target - current_value.
2. find rest in a dictionary. 
3. be careful about the same index of rest and current_value. 

### Code

```python
# created by Ji Wang ericshape @ 5/23/16 2:11 PM

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = dict()

        k = 0
        for v in nums:
            sum[v] = k
            k += 1

        k = 0
        for v in nums:
            rest = target - v
            # be careful about the result in same index!
            if rest in sum and k != sum[rest]:
                return [k, sum[rest]]
            k += 1
```

### Leetcode output
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 56 ms
Submitted: 0 minutes ago

```

### Reference
None

## 1. Two Sum 

```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
```

### Idea

1. rest = target - current_value.
2. find rest in a dictionary. 
3. be careful about the same index of rest and current_value. 

### Code

```python
# created by Ji Wang ericshape @ 5/23/16 2:11 PM

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = dict()

        k = 0
        for v in nums:
            sum[v] = k
            k += 1

        k = 0
        for v in nums:
            rest = target - v
            # be careful about the result in same index!
            if rest in sum and k != sum[rest]:
                return [k, sum[rest]]
            k += 1
```

### Leetcode output
```
16 / 16 test cases passed.
Status: Accepted
Runtime: 56 ms
Submitted: 0 minutes ago

```

### Reference
None
