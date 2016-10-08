"""
https://leetcode.com/problems/largest-rectangle-in-histogram/
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""

#O(N) algorithm
#http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
#http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
#https://siddontang.gitbooks.io/leetcode-solution/content/array/largest_rectangle_in_histogram.html
#http://fisherlei.blogspot.com/2012/12/leetcode-largest-rectangle-in-histogram.html
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #return self.divide_and_conquer(heights, 0, len(heights)-1)
        return self.linear(heights)
    
    def linear(self, heights):
        #get the left most and right most for each bar
        #使用栈，当前高度大于栈顶高度时，入栈； 如果栈顶高度高，说明栈顶元素最右的是当前元素，出站，继续比较栈顶和当前元素
        #总结：如果一个元素要pop出来，最右的肯定是当前元素前面那个位置，最左的是栈里下一个元素
        if len(heights) == 0: return 0
        length = len(heights)
        stack = []
        stack.append(0)
        maxh = heights[0]
        for cur in range(1, length):
            if heights[ stack[-1] ]<= heights[cur]:
                stack.append(cur)
            else:
                while len(stack)>0 and heights[ stack[-1]] > heights[cur]:
                    bar_index = stack.pop()
                    right_most = cur-1
                    left_most = stack[-1]+1 if len(stack)>0 else 0
                    bar_area = (right_most - left_most + 1) * heights[bar_index]
                    if maxh < bar_area:
                        maxh = bar_area
                    # bar_index, bar_area
                stack.append(cur)
        
        #at the end, the right most is length-1
        while len(stack)>0:
            bar_index = stack.pop()
            left_most =  stack[-1]+1 if len(stack)>0 else 0
            right_most = length -1    
            bar_area = (right_most - left_most + 1) * heights[bar_index]
            if maxh< bar_area:
                maxh = bar_area
            #print bar_index, bar_area
        return maxh
    
    """
    We can use Divide and Conquer to solve this in O(nLogn) time. The idea is to find the minimum value in the given array. Once we have index of the minimum value, the max area is maximum of following three values.
    a) Maximum area in left side of minimum value (Not including the min value)
    b) Maximum area in right side of minimum value (Not including the min value)
    c) Number of bars multiplied by minimum value.
    """
    def divide_and_conquer(self, heights, start_index, end_index):
        if not heights or start_index > end_index or start_index < 0 or end_index >= len(heights): return 0
        #print start_index, end_index
        index, minval = min( enumerate(heights[start_index:end_index+1]), key = lambda x: x[1])
        index = start_index + index
        cur_min_rec = (end_index-start_index +1 ) * minval
        left_min_rec = self.divide_and_conquer(heights, start_index, index-1)
        right_min_rec = self.divide_and_conquer(heights, index+1, end_index)
        return max( left_min_rec, right_min_rec, cur_min_rec)
    
