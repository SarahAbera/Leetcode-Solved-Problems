# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def dfs(node):
            if not node:
                return

            if node.val % 2 == 0:
                add(node)

            dfs(node.left)
            dfs(node.right)

        totalSum = 0
        def add(node):
            nonlocal totalSum
            left_child, right_child = node.left, node.right
            grand_children = []
            if left_child:
                left_grand_child1 = grand_children.append(left_child.left)
                left_grand_child2 = grand_children.append(left_child.right)
            if right_child:
                right_grand_child1 = grand_children.append(right_child.left)
                right_grand_child2 = grand_children.append(right_child.right)
            
            for child in grand_children:
                if child:
                    totalSum += child.val
        dfs(root)
        
        return totalSum
