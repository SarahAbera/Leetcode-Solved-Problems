class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        graph = defaultdict(list)
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        ans = [0] * n
        visited = set()
        def dfs(node):
            visited.add(node)
            count = defaultdict(int)
            count[labels[node]] = 1
            for child in graph[node]:
                if child in visited:
                    continue

                child_count = dfs(child)
                for i in child_count.keys():
                    count[i] += child_count[i]
            
            ans[node] = count[labels[node]]
            return count

        dfs(0)
        return ans
            
