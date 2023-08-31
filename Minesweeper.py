class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        directions = [(1,0),(0,1),(-1,0),(0,-1),(-1,1),(-1,-1),(1,-1),(1,1)]
        
        inbound = lambda r,c : 0 <= r < len(board) and 0 <= c < len(board[0])
        visited = set()
        def dfs(row,col):
            if board[row][col] != "E":
                return
            
            count = 0
            for dx,dy in directions:
                newr , newc = dx + row , dy + col
                if inbound(newr,newc):
                    if board[newr][newc] == "M":
                        count += 1

            if count > 0:
                board[row][col] = str(count)
                return
            board[row][col] = "B"

            for dx,dy in directions:
                newr , newc = dx + row , dy + col
                if inbound(newr,newc):
                    dfs(newr,newc)

        dfs(click[0],click[1])
        return board
            

        
