class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        running_sum = 0
        ans = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            ans = max(ceil(running_sum/(i+1)), ans)

        return ans
