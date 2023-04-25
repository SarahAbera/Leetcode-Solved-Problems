class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        directions = [(0,-1),(-1,0),(1,0),(0,1)]
        visited = set()
        def dfs(i,j,vertex):
            if (i < 0 or i == len(board)) or (j < 0 or j == len(board[0])) or board[i][j] == "X":
                return
            
            vertex.add((i,j))
            visited.add((i,j))
            for r, c in directions:
                if (i+r,j+c) not in visited:
                    dfs(i + r, j + c, vertex)

        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                vertex = set()
                if (i,j) not in visited:
                    dfs(i,j,vertex)
                    if vertex:
                        flag = True
                        for row, col in vertex:
                            if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1 :
                                flag = False
                                break

                        if flag:
                            for x, y in vertex:
                                board[x][y] = "X"
