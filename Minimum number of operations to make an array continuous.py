class Solution:
    def minOperations(self, nums: List[int]) -> int:
        duplicates = len(nums) - len(set(nums))
        n = len(nums) -1

        def bisectRight(arr,val):
            left = 0 
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > val:
                    right = mid - 1
                elif arr[mid] < val:
                    left = mid + 1
                else: return mid + 1
            return left

        nums_ = list(set(nums))
        nums_.sort()
        ans = inf
        for i in range(len(nums_)):
            expected_max = n + nums_[i]
            right_bound = bisectRight(nums_,expected_max)
            ans = min(len(nums_) - (right_bound - i), ans)
        return ans + duplicates
