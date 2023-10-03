class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        inbound = lambda x, y : 0 <= x < n and 0 <= y < n
        least_time = 0
        pq = [(grid[0][0],(0,0))]
        heapify(pq)
        visited = set()
        while pq:
            time, cell = heappop(pq)
            r , c = cell
            visited.add(cell)
            least_time = max(least_time,time)
            if (r,c) == (n-1, n-1):
                return least_time
            for dx,dy in directions:
                new_r = r + dx
                new_c = c + dy
                if inbound(new_r,new_c) and (new_r, new_c) not in visited:
                    heappush(pq,(grid[new_r][new_c], (new_r,new_c)))
      
