class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        def generate_subset(idx,arr):
            subsets.append(arr[:])

            for i in range(idx,len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                generate_subset(i+1,arr)
                arr.pop()
                
        generate_subset(0,[])
        return subsets
            
