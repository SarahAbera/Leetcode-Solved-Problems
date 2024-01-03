class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dp(buy,idx,transaction):
            if idx == len(prices) or transaction == 0:
                return 0
            if not buy:
                return max(
                    prices[idx] + dp(1,idx+1,transaction-1),
                    dp(0,idx+1,transaction)
                )
            return max(
                dp(0,idx+1,transaction) - prices[idx],
                dp(1,idx+1,transaction)
            )
        
        return dp(1,0,2)
     