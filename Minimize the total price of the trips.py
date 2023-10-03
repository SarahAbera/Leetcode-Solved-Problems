class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        n = len(price)
        g = defaultdict(list)
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
            
        result = []
        count = [0] * n
        def dfs(node, target, parent):
            result.append(node)
            
            if node == target:
                while result: count[result.pop()] += 1
                return True
            
            for neighbor in g[node]:
                if neighbor != parent:
                    if dfs(neighbor, target, node): return True
            
            result.pop()
            return False

        @lru_cache(None)
        def calc(node = 0, p = -1, h = False):
            res1 = count[node] * price[node]
            res2 = res1 // 2

            for adj in g[node]:
                if adj != p:
                    res1 += calc(adj, node, False)
            if h: return res1

            for adj in g[node]:
                if adj != p:
                    res2 += calc(adj, node, True)
            return min(res1, res2)


        for u, v in trips:
            dfs(u, v, -1)

        return calc()
