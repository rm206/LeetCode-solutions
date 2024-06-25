# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def process(node):
            nonlocal curr_sum
            if not node:
                return
            
            process(node.right)

            curr_sum += node.val
            node.val = curr_sum

            process(node.left)
        
        curr_sum = 0
        process(root)

        return root