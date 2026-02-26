# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0, True
            left_h, left_bal = dfs(node.left)
            right_h, right_bal = dfs(node.right)
            return 1 + max(left_h, right_h), left_bal and right_bal and abs(left_h-right_h)<=1
        
        _, is_bal = dfs(root)
        return is_bal