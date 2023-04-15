# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        count = 0
        def countPath(root,prefix,cur_sum):
            nonlocal count
            if not root:
                return
            
            prefix.append(cur_sum)
            cur_sum += root.val
            
            value = cur_sum - targetSum
            if value in prefix:
                count += prefix.count(value)
            
            countPath(root.left,prefix,cur_sum)
            countPath(root.right,prefix,cur_sum)
            cur_sum -= root.val
            prefix.pop()
            
        countPath(root,[],0)

        return count
