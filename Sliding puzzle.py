class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        path = 0 
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def get_zero_location(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        return (i, j)

        def inbound(i,j):
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                return True
            return False
                
        def to_tuple(board):
            return (tuple(board[0]), tuple(board[1]))
        def to_list(t):
            return [list(t[0]), list(t[1])]
        q = deque([to_tuple(board)])
        visited = {to_tuple(board)}
        ans = 0
        while q:

            for _ in range(len(q)):
                node = to_list(q.popleft())
                if node == [[1,2,3],[4,5,0]]:
                    return path
    
                x, y = get_zero_location(node)

                for dx, dy in directions:
                    newx = x + dx
                    newy = y + dy
                    if inbound(newx,newy):
                        new_node = [row[:] for row in node]
                        new_node[x][y], new_node[newx][newy] = new_node[newx][newy], new_node[x][y]
                        tup = to_tuple(new_node)
                        if tup not in visited:
                            q.append(tup)
                            visited.add(tup)
            path += 1

        return -1
        
