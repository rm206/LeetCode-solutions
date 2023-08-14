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
            
            if p.val == node.val or q.val == node.val:
                return node
            
            left = solver(node.left)
            right = solver(node.right)
            
            if left and right:
                return node
            elif left and not right:
                return left
            else:
                return right
            
            
        
        return solver(root)