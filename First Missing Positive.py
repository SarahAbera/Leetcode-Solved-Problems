class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        nums = set(nums)
        for i in range(1,100000000 + 1):
            if i not in nums:
                return i
