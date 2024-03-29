# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def solver(node, left, right):
            if not node:
                return True
            
            if node.val <= left or node.val >= right:
                return False
            
            return solver(node.left, left, node.val) and solver(node.right, node.val, right)
        
        left, right = float('-inf'), float('inf')
        return solver(root, left, right)