from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        colors = [0] * (n + 1)
        
        def dfs(person, color):
            colors[person] = color
            
            for neighbor in graph[person]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
            
            return True
        
        for i in range(1, n + 1):
            if colors[i] == 0 and not dfs(i, 1):
                return False
        
        return True
