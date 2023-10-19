class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxi = max(nums) - k
        mini = min(nums) + k
        if mini > maxi:
            return 0
        return maxi - mini
