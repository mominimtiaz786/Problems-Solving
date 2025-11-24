class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_yet = prices[0]
        max_profit = 0

        for p in prices:
            profit = p - min_yet
            max_profit = max(max_profit, profit)
            min_yet = min(min_yet, p)
        return max_profit