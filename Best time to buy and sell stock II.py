class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        
        def profit(idx, stock):
            if idx == len(prices):
                return 0
            
            if (idx, stock) in memo:
                return memo[(idx, stock)]
            
            if stock:
                memo[(idx, stock)] = max(profit((idx+1), 0) + prices[idx], profit((idx+1), 1))
            else:
                memo[(idx, stock)] = max(profit((idx+1), 1) - prices[idx], profit((idx+1), 0))

            return memo[(idx, stock)]
        
        return profit(0,0)
