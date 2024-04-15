# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solver(node, prev):
            nonlocal res
            
            curr = prev*10 + node.val
            
            if not node.left and not node.right:
                res += int(curr)
                return
                
            if node.left:
                solver(node.left, curr)
            if node.right:
                solver(node.right, curr)  
            
        res = 0
        solver(root, 0)
        return res