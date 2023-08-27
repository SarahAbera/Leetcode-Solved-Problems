"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(nod):
            if not nod:
                return None
            
            if nod not in oldToNew:
                oldToNew[nod] = Node(nod.val)
            for ngh in nod.neighbors:
                if ngh not in oldToNew:
                    dfs(ngh)
        dfs(node)
        
        for key,val in oldToNew.items():
            for ngh in key.neighbors:
                val.neighbors.append(oldToNew[ngh])

        return oldToNew[node] if node else []
