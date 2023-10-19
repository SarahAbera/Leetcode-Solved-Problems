class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        nums = [True for _ in range(n)]
        nums[0], nums[1] = False, False

        i = 2
        while i * i < n:
            if nums[i]:
                for j in range(2*i, n, i):
                    nums[j] = False
            i += 1

        return sum(nums)
        
