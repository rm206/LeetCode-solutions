# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def solver(node):
            if not node:
                return
            
            solver(node.left)
            solver(node.right)
            
            node.left, node.right = node.right, node.left
        
        solver(root)
        return root