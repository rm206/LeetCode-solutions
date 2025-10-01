# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not p or not q or not node:
                return None
            
            if (p.val < node.val < q.val) or (q.val < node.val < p.val):
                return node
            
            if node == p or node == q:
                return node

            if node.val < p.val and node.val < q.val:
                return dfs(node.right)
            
            else:
                return dfs(node.left)
        
        return dfs(root)