class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i:i for i in range(1,len(edges) + 1)}
        removableEdge = [0,0]
        def find(x):
            if x == parent[x]:
                return x

            root = find(parent[x])
            parent[x] = root
            return root

        def union(x,y):
            
            x_rep = find(x)
            y_rep = find(y)

            if y_rep == x_rep:
                removableEdge[0] = x
                removableEdge[1] = y

            parent[y_rep] = x_rep

        for start,end in edges:
            union(start,end)

        return removableEdge
