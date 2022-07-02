class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        buy_price = prices[0]
        
        for i in range(n-1):
            if prices[i+1] < prices[i]:
                profit += prices[i] - buy_price
                buy_price = prices[i+1]
        
        profit += prices[-1] - buy_price
        return profit