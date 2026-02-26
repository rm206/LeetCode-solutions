# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            lsum = max(0, dfs(node.left))
            rsum = max(0, dfs(node.right))
            res = max(res, node.val + lsum + rsum)
            return node.val + max(lsum, rsum)
        
        res = -math.inf
        dfs(root)
        return res