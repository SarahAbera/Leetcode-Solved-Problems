class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        global_ans = set()
        def backtrack(arr,indx):
            if len(arr) > 1:
                global_ans.add(tuple(arr[:]))
                

            for i in range(indx,len(nums)):
                if not arr or nums[i] >= arr[-1]:
                    arr.append(nums[i])
                    backtrack(arr,i+1)
                    arr.pop()
    
        backtrack([],0)
        return global_ans
