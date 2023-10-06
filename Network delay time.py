class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for s,d,t in times:
            graph[s].append((d,t))
        
        nodes = [inf for _ in range(n)]
        visited = set()
        pq = [(0,k)]
        while pq:
            time,node = heappop(pq)
            if node in visited:
                continue
            
            visited.add(node)
            nodes[node-1] = time
            for child,weight in graph[node]:
                heappush(pq,(weight + time, child))

        return -1 if max(nodes) == inf else max(nodes)

