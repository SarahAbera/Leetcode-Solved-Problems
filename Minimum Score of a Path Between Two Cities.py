class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = {i:i for i in range(1,n+1)}
        cost = {i:inf for i in range(1,n+1)}
        size = {i:1 for i in range(1,n+1)}
        def find(child):
            while parent[child] != child:
                child = parent[child]
            return child

        def union(x,y,dist):
            x_rep = find(x)
            y_rep = find(y)
            
            if size[x_rep] >= size[y_rep]:
                cost[x_rep] = min(cost[x_rep],dist,cost[y_rep])
                parent[y_rep] = x_rep
                size[x_rep] += y_rep
            else:
                cost[y_rep] = min(cost[x_rep],dist,cost[y_rep])
                parent[x_rep] = y_rep
                size[y_rep] += x_rep

        for start,end,dist in roads:
            union(start,end,dist)
        return cost[find(1)]
