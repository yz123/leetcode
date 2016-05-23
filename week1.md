# 1st Week Report
Ji Wang

## 0. Task
- [x] #1 Two Sum [link](https://leetcode.com/problems/two-sum/)
- [ ] #题号 题目名称 [link](URL) 

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

## 2. #题号 题目 
分类：数组？String？simple?
```
题目叙述
```

### Idea
input your idea here.

### Code
python

```python
class PythonCodeHere():
  pass
```

### Leetcode output
```
leetcode output here
```

### Reference
1. reference 1 [link1](link1)
2. reference 2 [link2](link2)
3. 
