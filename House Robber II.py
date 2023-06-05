class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        memo=[-1 for _ in range(len(nums))]
        def dp(i):
            if i<0:
                return 0 
            elif memo[i]>=0:
                return  memo[i]
            else:
                res=max(dp(i-2)+nums[i],dp(i-1))
                memo[i]=res
                return res
        a=dp(len(nums)-2)
        memo=[-1 for _ in range(len(nums))]
        nums.pop(0)
        b=dp(len(nums)-1)
        return max(a,b)
