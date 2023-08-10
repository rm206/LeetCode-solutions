# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def solver(node):
            nonlocal res
            
            if not node:
                return 0
            
            left = solver(node.left)
            right = solver(node.right)
            
            res = max(res, left + right)
            
            return 1 + max(left, right)
        
        res = 0
        solver(root)
        return res