class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        lowercase = list(string.ascii_lowercase)
        parent = {i:i for i in lowercase}

        def find(char):
            if char == parent[char]:
                return char

            root = find(parent[char])
            parent[char] = root
            return root

        def union(x,y):
            rep1 = find(x)
            rep2 = find(y)
            
            order = [rep1, rep2]
            order.sort()
            parent[order[1]] = order[0]

        for i in range(len(s1)):
            union(s1[i],s2[i])
        
        answer = ""
        for char in baseStr:
            answer += find(char)

        return answer
