# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node, curr_max):
            if not node:
                return 0
            
            res = 1 if node.val >= curr_max else 0
            curr_max = max(curr_max, node.val)
            
            res += helper(node.left, curr_max)
            res += helper(node.right, curr_max)
            
            return res
        
        return helper(root, root.val)
        
        