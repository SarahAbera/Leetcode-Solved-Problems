class Solution:
    def knightDialer(self, n: int) -> int:
        hashmap = {0:(4,6), 1:(6,8), 2:(7,9), 3:(8,4), 4:(3,9,0), 
                    5:[], 6:(0,1,7), 7:(6,2), 8:(1,3), 9:(2,4) 
        }

        @cache
        def dp(start,n):
            if n == 1:
                return 1
            ans = 0
            for ngh in hashmap[start]:
                n -= 1
                ans += dp(ngh, n)
                n += 1

            return ans

        res = 0
        for i in range(10):
            res += dp(i,n)
        return res % (10**9 + 7)
        
