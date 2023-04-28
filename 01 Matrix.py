class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        inbound = lambda cell: 0 <= cell[0] < len(mat) and 0 <= cell[1] < len(mat[0])
        
        def bfs():
            queue = deque()
            visited = set()
            m, n = len(mat), len(mat[0])
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == 0:
                        queue.append((i,j))
                        visited.add((i,j))

                    else:
                        mat[i][j] = "*"
            while queue:
                r, c = queue.popleft()    
                for dr,dc in directions:
                    nr = dr + r
                    nc = dc + c
                
                    if inbound((nr,nc)) and (nr,nc) not in visited:
                        mat[nr][nc] = mat[r][c] + 1
                        queue.append((nr,nc))
                        visited.add((nr,nc))
        
        
        bfs()
        return mat
