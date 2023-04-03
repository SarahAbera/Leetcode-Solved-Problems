class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0

        while x or y:
            i = x & 1
            j = y & 1

            if i != j:
                count += 1
            
            x >>= 1
            y >>= 1
        
        return count
