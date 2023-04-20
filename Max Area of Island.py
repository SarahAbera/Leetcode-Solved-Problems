class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def maxArea():
            max_area = 0
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    value = grid[row][col]
                    if value == 1:
                        current_area = dfs(row,col)
                        max_area = max(current_area,max_area)
        
            return max_area

        def inbound(new_row,new_col):
            return 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])


        def dfs(row,col):
            stack = []
            area = 0
            stack.append((row,col))
            grid[row][col] = 0
            
            while stack:
                area += 1
                
                row,col = stack.pop()
                for r, c in directions:
                    new_row = row + r
                    new_col = col + c
                    
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        stack.append((new_row,new_col))
                        grid[new_row][new_col] = 0

            cur_area = area
            area = 0
            return cur_area

        return maxArea()
