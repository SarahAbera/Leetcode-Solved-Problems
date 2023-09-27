class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(ages, scores))
        players.sort()
        
        memo = {}
        def dp(i):
            if i==0:
                return players[i][1]
            if i in memo:
                return memo[i]
            max_value = 0
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    max_value = max(max_value, dp(j))
            memo[i] = max_value + players[i][1]
            return memo[i]
        return max(dp(i) for i in range(len(scores)))
