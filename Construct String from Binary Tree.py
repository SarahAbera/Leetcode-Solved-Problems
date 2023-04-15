# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        string = []
        def preorder(root):
            if not root:
                return

            string.append("(")
            string.append(str(root.val))
            if not root.left and root.right:
                string.append("()")
            preorder(root.left)
            preorder(root.right)
            string.append(")")
            
        preorder(root)
        string = "".join(string)
        return string[1:-1]
