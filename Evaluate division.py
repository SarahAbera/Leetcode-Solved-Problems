class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a,b = eq
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))

        def bfs(src,target):
            if src not in adj or target not in adj:
                return -1

            q = deque([(src,1)])
            visited = {src}

            while q:
                node, wei = q.popleft()
                if node == target:
                    return wei
                
                for ngh,weight in adj[node]:
                    if ngh not in visited:
                        q.append((ngh,wei * weight))
                        visited.add(ngh)

            return -1

        return [bfs(n1,n2) for n1,n2 in queries]
        
