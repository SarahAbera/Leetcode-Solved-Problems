class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)
        for i in range(len(edges)):
            adjList[edges[i][0]].append((edges[i][1],-succProb[i]))
            adjList[edges[i][1]].append((edges[i][0],-succProb[i]))
        
        queue = [(-1,start_node)]
        heapify(queue)
        visited = set()
        max_probability = -1
        while queue:
            prob,node = heappop(queue)
            if node == end_node:
                max_probability = max(-prob,max_probability)
            else:
                visited.add(node)

            for nxt,curProb in adjList[node]:
                if nxt not in visited:
                    heappush(queue,(-(prob * curProb), nxt))
        return max_probability if max_probability != -1 else 0
