"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = {}
        for employee in employees:
            i = employee.id
            importance = employee.importance
            subordinate = employee.subordinates
            graph[i] = (importance,subordinate)
        
        count = 0
        def dfs(id):
            nonlocal count
            count += graph[id][0]
            for subordinate in graph[id][1]:
                dfs(subordinate)

        dfs(id)
        return count
