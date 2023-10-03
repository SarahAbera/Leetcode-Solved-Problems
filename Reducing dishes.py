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

# dp top down solution
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        @cache
        def dp(index, time):
            if index > len(satisfaction) - 1:
                return 0
            
            return max(satisfaction[index] * time + dp(index + 1, time + 1), dp(index + 1, time))
        
        return dp(0, 1)
        
