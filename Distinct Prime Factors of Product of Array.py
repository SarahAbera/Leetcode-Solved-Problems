class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        distinct_nums = set()

        for x in nums:

            t = 2
            while t * t <= x:
                while x % t == 0:
                    x //= t
                    distinct_nums.add(t)

                t += 1

            if x > 1:
                distinct_nums.add(x)

        return len(distinct_nums)
                    
