class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        totalTo_b = sum(cost[1] for cost in costs)
        
        
        diff = [cost[0] - cost[1] for cost in costs]
        diff.sort()
        
        num_of_people = len(costs)
        i = num_of_people//2
        j = 0
        while i > 0:
            totalTo_b += diff[j]
            j += 1
            i -= 1
        return totalTo_b
