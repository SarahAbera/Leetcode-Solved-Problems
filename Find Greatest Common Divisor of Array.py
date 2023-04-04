class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_ = max(nums)
        min_ = min(nums)

        def GCD(a,b):
            if b == 0:
                return a

            return GCD(b, a % b)
        
        return GCD(max_, min_)
