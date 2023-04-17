class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        indegrees = set()
        for start,end in edges:
            indegrees.add(end)
        ans = []
        for i in range(n):
            if i not in indegrees:
                ans.append(i)

        return ans
