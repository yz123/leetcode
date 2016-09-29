"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

#http://bangbingsyb.blogspot.com/2014/11/leetcode-gas-station.html
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        totalsum, cursum, start = 0, 0, 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            totalsum += diff
            cursum += diff
            if cursum < 0 :
                start = i+1
                cursum = 0
        print totalsum
        if totalsum<0:
            return -1
        
        return start
        
