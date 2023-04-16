class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutation = []
        arr = []
        def permuting():
            if len(arr) == len(nums):
                permutation.append(arr[:])
                return
            
            for i in range(0, len(nums)):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    permuting()
                    arr.pop()

        permuting()
        return permutation
