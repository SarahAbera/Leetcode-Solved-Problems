class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def numOfIslands():
            count = 0
            visited = set()
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    value = grid[row][col]
                    if (row,col) not in visited and value == "1":
                        dfs(row,col,visited)
                        count += 1
            
            return count

        def inbound(new_row,new_col):
            return 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])
        
        def dfs(row,col,visited):
            if grid[row][col] == "1":
                visited.add((row,col))
            
            for r, c in directions:
                new_row = row + r
                new_col = col + c

                if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == "1":

                    dfs(new_row,new_col,visited)

        return numOfIslands()
