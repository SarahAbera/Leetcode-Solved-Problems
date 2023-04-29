class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        len_row, len_col = len(maze), len(maze[0])
        inbound = lambda cell: 0 <= cell[0] < len_row and 0 <= cell[1] < len_col

        queue = deque([(entrance[0], entrance[1])])
        visited = {(entrance[0], entrance[1])}
        nearest_exit_steps = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    newr, newc = dr + r, dc + c
                    if (newr,newc) not in visited and inbound((newr,newc)):
                        if maze[newr][newc] == ".":
                            if newr == 0 or newr == len_row - 1 or newc == 0 or newc == len_col - 1:
                                return nearest_exit_steps + 1
                            queue.append((newr,newc))
                            visited.add((newr,newc))

            nearest_exit_steps += 1

        return -1
