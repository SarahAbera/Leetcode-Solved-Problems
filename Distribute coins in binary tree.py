# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        count = 0
        def helper(node):
            nonlocal count
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            if left < 0:
                count += abs(left)
            if right < 0:
                count += abs(right)
            curr_node = left + right + node.val
            if curr_node > 1:
                count += (curr_node-1)
            
            return curr_node - 1
        helper(root)
        return count
            
        
