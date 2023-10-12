class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 1
        for i in range(1,n+1):
            ans *= (2 * i -1) * i
        return ans % MOD
        
