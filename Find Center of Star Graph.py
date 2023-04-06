class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b= edges[0]
        c, d = edges[1]
        if a == c:
            return a
        elif a == d:
            return a
        elif b == c:
            return b
        else:
            return d
