# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def comp(left, right):
            if not left and not right:
                return True
            
            if (left and not right) or (right and not left):
                return False
            
            return (left.val == right.val) and comp(left.left, right.right) and comp(left.right, right.left)
        
        if not root:
            return True
        
        return comp(root.left, root.right)