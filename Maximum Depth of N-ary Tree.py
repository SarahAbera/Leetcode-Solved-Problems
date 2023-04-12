"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        count = 0
        numNodes = 1
        def dfs(root):
            nonlocal count
            nonlocal numNodes
            if not root:
                return

            if not(root.children):
                count = max(numNodes,count)
                numNodes -= 1
                return
            
            for child in root.children:
                numNodes += 1
                dfs(child)
            
            numNodes -= 1

        dfs(root)
        return count
