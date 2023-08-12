# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            # Base case: node is None
            if not node:
                return 0
            
            # Get the maximum sum of the left subtree
            left_sum = max(dfs(node.left), 0)
            # Get the maximum sum of the right subtree
            right_sum = max(dfs(node.right), 0)
            
            # Update the maximum path sum so far with the sum of the current node
            # and the maximum sums of the left and right subtrees
            self.max_path_sum = max(self.max_path_sum, node.val + left_sum + right_sum)
            
            # Return the maximum sum of the current node and the maximum sum of its
            # left and right subtrees
            return node.val + max(left_sum, right_sum)
        
        # Initialize the maximum path sum to negative infinity
        self.max_path_sum = float('-inf')
        
        # Start the depth-first search
        dfs(root)
        
        # Return the maximum path sum
        return self.max_path_sum
