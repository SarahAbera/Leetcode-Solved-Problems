class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sorted_ = sorted(nums)
        if sorted_ == nums or sorted_[::-1] == nums:
            return True
        
        return False
        