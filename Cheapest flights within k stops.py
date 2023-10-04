class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for start,dest,weight in flights:
            adjList[start].append((dest,weight))
        
        pq = [(0,0,src)]
        heapify(pq)
        visited = set()
        while pq:
            price, m, node = heappop(pq)
            
            if (node,m) in visited:
                continue
            visited.add((node,m))
            if node == dst:
                return price

            for child,weight in adjList[node]:
                if child == dst and (child, m) not in visited:
                    heappush(pq, (price + weight, m, child))

                else:
                    if m < k and (child, m + 1) not in visited:
                        heappush(pq, (price + weight, m + 1, child))

        return -1
