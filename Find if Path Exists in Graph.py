class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = defaultdict(int)
        for i in range(n):
            parent[i] = i

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(x,y):
            x_parent = find(x)
            y_parent = find(y)
            parent[y_parent] = x_parent

        for start, end in edges:
            union(start,end)

        return find(source) == find(destination)
