# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        paths = []
        def dfs(root,cur_path):
            cur_path.append(str(root.val))

            if not root.left and not root.right:
                paths.append("".join(cur_path))
                return
            if root.left:
                dfs(root.left, cur_path)
                cur_path.pop()
            if root.right:
                dfs(root.right, cur_path)
                cur_path.pop()

        dfs(root,[])    
        total_sum = sum(list(map(int,paths)))
        return total_sum    
