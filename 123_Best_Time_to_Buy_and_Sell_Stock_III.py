"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

#http://www.cnblogs.com/yrbbest/p/4438472.html
"""
一上来就没有头绪，查了一些资料以后发现大家都是用dp，可是怎么用dp才能又简洁又漂亮。不少朋友都是用类似Best Time to Buy and Sell Stock I的方法，正序来一次，逆序再来一次，然后求解，这样可以解决只能卖2次的情况。这个方法也跟Trap Rain Water很像。
"""

"""
 profit = Math.max(profit, prices[i] - minPrice);
 oneTransProfit[i] = profit;
 minPrice = Math.min(minPrice, prices[i]);
"""

#reversse
""
 profit = Math.max(profit, maxPrice-prices[i]);
 secondTransProfit[i] = profit;
 maxPrice = Math.max(maxPrice, prices[i]); 
""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
            
        length = len(prices)
        profit = [ 0 for i in range(length) ]
        
        pro = 0
        cur_min = prices[0]
        for i in range(1, length):
            price = prices[i]
            if price < cur_min:
                cur_min = price
            elif price > cur_min:
                curpro = price -cur_min
                if curpro > pro:
                    pro = curpro
            profit[i] = pro
        
        max_one_trans = pro
        
        cur_max = prices[length-1]
        secpro = 0
        maxpro = profit[length-2]+ secpro
        #check the profit 
        for i in range(length-2, 0, -1):
            price = prices[i]
            if price > cur_max:
                cur_max = price
            elif price < cur_max:
                curpro = cur_max -price
                if curpro > secpro:
                    secpro = curpro
            pro_from_i_to_end = secpro
            #  profit[i---end]+ profit[---(i-1)]
            if pro_from_i_to_end + profit[i-1] > maxpro:
                maxpro = pro_from_i_to_end + profit[i-1]
                
        return max( maxpro, max_one_trans)
        
