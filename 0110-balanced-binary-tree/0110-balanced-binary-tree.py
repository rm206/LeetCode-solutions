# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            if not node:
                return [True, 0]
            
            isLeftBalanced, leftHeight = helper(node.left)
            isRightBalanced, rightHeight = helper(node.right)
            
            balanced = isLeftBalanced and isRightBalanced and abs(leftHeight - rightHeight) <= 1
            
            return [balanced, 1 + max(leftHeight, rightHeight)]
        
        return helper(root)[0]