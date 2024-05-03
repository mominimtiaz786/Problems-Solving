class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minYet = prices[0]
        for p in prices:
            minYet = min(minYet, p)
            maxProfit = max(maxProfit, p - minYet)
        
        return maxProfit