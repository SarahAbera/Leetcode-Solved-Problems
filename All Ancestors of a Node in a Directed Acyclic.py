class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [set() for _ in range(n)]
        graph = defaultdict(list)
        indegree = [0] * n
        for start,goal in edges:
            graph[start].append(goal)
            indegree[goal] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                answer[nei].add(node)
                answer[nei].update(answer[node])
                
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        for i in range(n):
            answer[i] = list(sorted((answer[i])))
        return answer
