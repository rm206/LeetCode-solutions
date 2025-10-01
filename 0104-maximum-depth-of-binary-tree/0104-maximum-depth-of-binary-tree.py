# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr):
            nonlocal res
            if not node:
                return
            
            res = max(res, curr)
            dfs(node.left, curr + 1)
            dfs(node.right, curr + 1)
        
        res = 0
        dfs(root, 1)
        return res