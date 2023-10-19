class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days.sort()
        @cache
        def dp(idx):
            if idx == len(days):
                return 0

            return min(costs[0] + dp(idx + 1),costs[1] + dp(bisect_right(days,days[idx] + 6)),costs[2] + dp(bisect_right(days, days[idx] + 29)))

        return dp(0)
        
