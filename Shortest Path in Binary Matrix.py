class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]
        
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        inbound = lambda cell: 0 <= cell[0] < len(grid) and 0 <= cell[1] < len(grid)
        
        path = 0
        
        
        queue = deque([(0,0)])
        visited = set((0,0))

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                
                
                if r == len(grid) - 1 and c == len(grid) - 1:
                    return path + 1

                for i,j in directions:
                    if inbound((i + r,j + c)) and grid[i + r][j + c] == 0 and (i + r,j + c) not in visited:
                        queue.append((i + r, j + c))
                        visited.add((i + r, j + c))
            path += 1
        return - 1
        
