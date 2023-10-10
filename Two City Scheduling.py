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

# solution 2
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        greedy = []
        for idx, cost in enumerate(costs):
            diff = cost[1] - cost[0]
            greedy.append((diff,idx))

        greedy.sort()
        min_cost = 0
        for i,cost in enumerate(greedy):
            diff, idx = cost
            if i >= len(greedy) // 2:
                min_cost += costs[idx][0]
            else:
                min_cost += costs[idx][1]
        
        return min_cost
        
