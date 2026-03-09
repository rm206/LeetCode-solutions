# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solver(node, max_so_far):
            nonlocal res
            if not node:
                return
            
            if node.val >= max_so_far:
                res += 1
            
            solver(node.left, max(max_so_far, node.val))
            solver(node.right, max(max_so_far, node.val))

        res = 0
        solver(root, -math.inf)
        return res