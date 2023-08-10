# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solver(node):
            
            if not node:
                return [0, True]
            
            left_ht, left_bal = solver(node.left)
            right_ht, right_bal = solver(node.right)
            
            bal = left_bal and right_bal and abs(left_ht - right_ht) <= 1
            new_ht = 1 + max(left_ht, right_ht)
            
            return [new_ht, bal]
        
        return solver(root)[1]