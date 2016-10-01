"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

#https://leetcode.com/articles/best-time-buy-and-sell-stock-ii/
#1 5 2 6 (a, b, c, d)   d-a   d-c + b-a = d-a + (b-c) 
#如果b>c, 如 5>2, 则永远是从小的找到最大的，然后再从小的到大的，这样利润最大

#look at the current element i, if p[i]>=p[i-1], keep doing; 
#if p[i]< p[i-1]:则：如果p[i-1]不是最小的那个元素， profit += p[i-1]-curmin;如果p[i-1]是当前最小，则把p[i]调到当前最小
"""
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
            
        profit = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            pre_p = prices[i-1]
            cur_p = prices[i]
            if cur_p < pre_p:
                #keep finding valley
                if pre_p == cur_min:
                    cur_min = cur_p
                #prevous is a peak    
                else:
                    profit += (pre_p - cur_min)
                    cur_min = cur_p
        if prices[-1]>=prices[-2]:
            profit += (prices[-1]-cur_min)
        
        return profit
"""

class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit += (prices[i]-prices[i-1])
        return profit
