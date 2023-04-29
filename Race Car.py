class Solution:
    def racecar(self, target: int) -> int:

        queue = deque([(0,1)])
        visited = set((0,1))
        shortest = 0
        while queue:

            for _ in range(len(queue)):
                position, speed = queue.popleft()
                if position == target:
                    return shortest
                
                if (position + speed, speed * 2) not in visited:
                    visited.add((position + speed, speed * 2))
                    queue.append((position + speed, speed * 2))
                if speed > 0:
                    if (position, -1) not in visited:
                        visited.add((position, -1))
                        queue.append((position, -1))

                else:
                    if (position,1) not in visited:
                        visited.add((position, 1))
                        queue.append((position, 1))

            shortest += 1
