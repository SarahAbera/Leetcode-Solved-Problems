class Solution:
    
    memo = defaultdict(int)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        if n <= 2:
            return 1
        
        if n not in self.memo.keys():
            self.memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
      
        return self.memo[n]
