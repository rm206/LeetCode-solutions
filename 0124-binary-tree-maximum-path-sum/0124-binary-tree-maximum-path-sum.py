# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal res

            if not node:
                return float("-inf")
            
            left = helper(node.left)
            right = helper(node.right)

            res = max(res, node.val, left + node.val, right + node.val, left + node.val + right)
            max_passing_through_node = max(left + node.val, right + node.val, node.val)
            return max_passing_through_node
        
        res = float("-inf")
        helper(root)
        return res