# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []

        # two types of nodes to be deleted: if root or if leaf
        def dfs(root):
            if root is None:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in to_delete:
                if root.left is None and root.right is None:
                    return None 
                else:
                    if root.left:
                        res.append(root.left)
                    if root.right:
                        res.append(root.right)
                    return None
            
            return root
        
        to_delete = set(to_delete)
        node = dfs(root)
        if node:
            res.append(node)
        return res