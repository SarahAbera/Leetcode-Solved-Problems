class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # find the maximum bitwise or of an arra
        max_bitOr = 0
        for num in nums:
            max_bitOr |= num

        # generate all possible combinations of an array with max_bitwise val
        res = 0
        def backtrack(idx,ans):
            nonlocal res
            if ans == max_bitOr:
                res +=1

            for i in range(idx,len(nums)):
                new_ans = ans | nums[i]
                backtrack(i+1,new_ans)
            
        backtrack(0,0)
        return resCo
