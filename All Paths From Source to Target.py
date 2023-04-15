class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph) - 1
        answer = []
        def dfs(path, idx):
            if idx == N:
                answer.append(path[:])
                return

            for node in graph[idx]:
                path.append(node)
                dfs(path,node)
                path.pop()

        dfs([0],0)
        return answer
