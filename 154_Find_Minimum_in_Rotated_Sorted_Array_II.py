#worst case: O(n)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = len(nums)-1
        while begin < end:
            middle = begin + (end - begin)/2
            #print middle
            if nums[middle] > nums[end]:
                begin = middle + 1
            elif nums[middle] < nums[end]:
                end = middle
            else:
                if nums[middle] > nums[begin]:
                    end = middle -1
                else: #nums[middle]== nums[begin] == nums[end] 左右都有可能
                    begin +=1
                    end -=1
                
        return nums[begin]
