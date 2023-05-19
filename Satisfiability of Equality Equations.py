class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        inequal_edges = []

        small_letter = list(string.ascii_lowercase)
        parent = {i:i for i in small_letter}

        def valid(x,y):
            if find(x) == find(y):
                return False
            return True
        
        def find(variable):
            if variable == parent[variable]:
                return variable

            root = find(parent[variable])
            parent[variable] = root
            return root

        def union(var1,var2):
            rep1 = find(var1)
            rep2 = find(var2)

            parent[rep2] = rep1
        
        for equation in equations:
            if equation[1] != "!":
                a = equation[0]
                b = equation[3]
                union(a,b)
            else:
                inequal_edges.append((equation[0], equation[3]))
        
        for a,b in inequal_edges:
            if not valid(a,b):
                return False
        return True
