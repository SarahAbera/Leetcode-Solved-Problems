class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        while n:
            y = n >> 1
            if n & 1 == y & 1:
                return False
            n >>= 1
        return True
