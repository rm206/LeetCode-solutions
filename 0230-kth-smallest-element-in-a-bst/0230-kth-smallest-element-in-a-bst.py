# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def solver(node):
            nonlocal ctr, res
            if not node:
                return
            
            solver(node.left)
            ctr += 1
            if ctr == k:
                res = node.val
            solver(node.right)
        
        res = None
        ctr = 0
        solver(root)
        return res