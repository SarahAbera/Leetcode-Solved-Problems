class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        arr = []
        
        for i in range(len(satisfaction)):
            arr.append(satisfaction[i:])

        ans = 0
        for lst in arr:
            like_time = 0
            for i in range(len(lst)):
                like_time += lst[i] * (i+1)
            ans = max(ans,like_time)

        return ans
                

        
