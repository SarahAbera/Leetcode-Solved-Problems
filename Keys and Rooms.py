class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        def bfs(first_key):
            queue = deque([first_key])
            while queue:
                key = queue.popleft()
                visited.add(key)

                for i in range(len(rooms[key])):
                    if rooms[key][i] not in visited:
                        queue.append(rooms[key][i])
                        
        bfs(0)
        
        return len(visited) == len(rooms)
