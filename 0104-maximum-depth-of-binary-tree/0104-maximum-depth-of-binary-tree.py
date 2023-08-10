# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solver(node):
            if not node:
                return 0
            
            left = solver(node.left)
            right = solver(node.right)
            
            return 1 + max(left, right)
        
        return solver(root)