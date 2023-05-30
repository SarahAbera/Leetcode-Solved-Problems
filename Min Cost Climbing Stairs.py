class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(idx):
            if idx >= len(cost):
                return 0
            
            if idx in memo:
                return memo[idx]
            
            memo[idx] = min(dp(idx+1), dp(idx+2)) + cost[idx]

            return memo[idx]

        return min(dp(0),dp(1))
