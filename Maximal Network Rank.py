class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) == 1:
            return 1
             
        store = defaultdict(set)
        for road in roads:
            store[road[0]].add(road[1])
            store[road[1]].add(road[0])

        length = 0
        for i in range(n-1):
            for j in range(i+1, n):
                is_edge = j in store[i]
                length = max(length,len(store[i]) + len(store[j]) - is_edge)
        return length
