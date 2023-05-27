class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        minDiff = inf
        nums.sort()
        n = len(nums)
        minDiff = min(minDiff, nums[n-2] - nums[2])   
        minDiff = min(minDiff, nums[n-1] - nums[3])
        minDiff = min(minDiff, nums[n-4] - nums[0])
        minDiff = min(minDiff, nums[n-3] - nums[1])  

        return minDiff    
       
