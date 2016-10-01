"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""

#找出最小的那个值，然后看前面最大的那个值，profit = 最大-最小
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
            
        profit =0
        cur_min = prices[0]
        
        for i in range(1, len(prices)):
            price = prices[i]
            if price < cur_min:
                cur_min=price
            elif price > cur_min:
                tmp = price-cur_min
                if tmp > profit:
                    profit = tmp
        return profit
        
        """
        if len(prices) < 2: return 0
        buy = prices[0]
        sale = 0
        profit = 0
        for i in xrange(len(prices)):
            if prices[i] < buy: #if item lower than buy, set as buy
                buy = prices[i]
            elif prices[i] > buy: 
                sale = prices[i]  
                if sale - buy > profit:
                    profit = sale - buy
        if sale == 0: return 0
        return profit
        """
