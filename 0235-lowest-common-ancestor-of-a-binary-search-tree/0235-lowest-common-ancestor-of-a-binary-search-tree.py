# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solver(node):
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left = solver(node.left)
            right = solver(node.right)

            if not left and not right:
                return None
            if left and not right:
                return left
            if right and not left:
                return right
            
            return node
        
        return solver(root)