class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i,e = 0, 1
        maxp = 0
        while e < len(prices):
            if prices[i] < prices[e]:
                maxp = max(maxp, prices[e] - prices[i])
            else:
                i = e

            e += 1
            
        
        return maxp