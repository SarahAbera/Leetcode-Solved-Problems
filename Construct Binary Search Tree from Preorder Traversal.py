# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        def insertNode(root,value):
            if value > root.val:
                if root.right is None:
                    root.right = TreeNode(value)
                    return
                insertNode(root.right,value)
            else:
                if root.left is None:
                    root.left = TreeNode(value)
                    return
                insertNode(root.left,value)

        for value in preorder[1:]:
            insertNode(root,value)
        return root
