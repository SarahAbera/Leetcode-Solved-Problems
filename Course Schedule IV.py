class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for prereq, crs in prerequisites:
            graph[crs].append(prereq)

        prereqMap = {}
        def dfs(crs):
            if crs in prereqMap:
                return prereqMap[crs]
            else:
                prereqMap[crs] = set()
                for ngh in graph[crs]:
                    prereqMap[crs] |= dfs(ngh)
                prereqMap[crs].add(crs)
            return prereqMap[crs]
                
        for n in range(numCourses):
            if n not in prereqMap:
                dfs(n)

        result = []
        for u, v in queries:
            result.append(u in prereqMap[v])

        return result
