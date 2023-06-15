# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []
        
        def helper(node):
            if node:
                helper(node.left)
                inOrder.append(node.val)
                helper(node.right)
                
        helper(root)
        print(inOrder)
        return inOrder[k - 1]