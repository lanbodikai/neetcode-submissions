class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        e = 1
        n = len(prices)
        maxp = 0
        while e < n:
            if prices[i] < prices[e]:
                maxp = max(maxp, prices[e] - prices[i])
            else:
                i = e

            e += 1
            
        
        return maxp