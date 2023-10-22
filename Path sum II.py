# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(node,runSum,curPath):
            if not node:
                return []

            curPath.append(node.val)
            runSum += node.val
            if runSum == targetSum and not node.right and not node.left:
                ans.append(curPath.copy())
                curPath.pop()
                runSum -= node.val
                return

            dfs(node.left,runSum, curPath)
            dfs(node.right,runSum, curPath)
            curPath.pop()
            runSum -= node.val

        dfs(root,0,[])
        return ans      
