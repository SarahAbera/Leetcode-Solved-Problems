class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = [(nums[i], i) for i in range(len(nums))]
        array.sort()

        left = 0
        right = len(nums) - 1
        
        while left < right:
            if array[left][0] + array[right][0] > target:
                right -= 1
            elif array[left][0] + array[right][0] < target:
                left += 1
            else:
                return array[left][1], array[right][1]
        
        