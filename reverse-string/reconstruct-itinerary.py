class Solution:
    def findItinerary(self, tickets):
        res = []
        adj = defaultdict(list)
        for u, v in tickets:
            heappush(adj[u],v)

        def dfs(cur):
            while adj[cur]:
                dst = heappop(adj[cur])
                dfs(dst)
            res.append(cur)

        dfs("JFK")
        return res[::-1]