class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0] * len(graph)
        answer = []
        def dfs(node):
            if colors[node] == 1:
                return False
            colors[node] = 1

            for ngh in graph[node]:
                if colors[ngh] != 2:
                    if not dfs(ngh):
                        return False
                
            colors[node] = 2
            answer.append(node)
            return True

        for node in range(len(graph)):
            if colors[node] == 0: #not processed yet
                dfs(node)
        
        return sorted(answer)       
