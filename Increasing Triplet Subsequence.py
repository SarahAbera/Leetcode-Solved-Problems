class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first_min = inf
        second_min = inf

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False
