class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        len_row, len_col = len(grid1), len(grid1[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        flag = True
        def dfs(r,c):
            nonlocal flag
            if (r < 0 or r == len_row) or (c < 0 or c == len_col) or grid2[r][c] != 1:
                return
            
            if grid2[r][c] == 1 and grid1[r][c] != 1:
                flag = False

            grid2[r][c] = 2

            for i,j in directions:
                dfs(r + i, c + j)
            

        count = 0
        for r in range(len_row):
            for c in range(len_col):
                if grid2[r][c] == 1:
                    flag = True
                    dfs(r,c)
                    if flag:
                        count += 1
        return count
