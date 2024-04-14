# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def solver(node, coming_to_left):
            if not node:
                return 0
            
            if not node.left and not node.right and coming_to_left:
                return node.val
            
            if not node.left and not node.right:
                return 0
            
            
            left_res = solver(node.left, True)
            right_res = solver(node.right, False)
            
            return left_res + right_res
        
        return solver(root, False)