class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        nums = [0]*(n+1)
        def build_nums(n):
            if n == 1 or n == 0:
                nums[n] = n
                return nums

            build_nums(n-1)
            idx = n//2
            if n % 2 == 0:
                nums[n] = nums[idx]
            else:
                nums[n] = nums[idx] + nums[idx + 1]

            return nums
        
        build_nums(n)
        # print(nums)
        return max(nums)
