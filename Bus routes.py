class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:  
        if target == source:
            return 0
        
        graph = defaultdict(set)
        for i,route in enumerate(routes):
            for r in route:
                graph[r].add(i)
                
        visited = {*graph[source]}
        Q = deque([*graph[source]])
        
        distance = 1
        while Q:
            for _ in range(len(Q)):
                path = Q.popleft()
                for r in routes[path]:
                    if target == r:
                        return distance
                    for stop in graph[r]:
                        if stop not in visited:
                            Q.append(stop)
                            visited.add(stop)
            distance += 1

        return -1
