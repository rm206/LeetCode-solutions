# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_sum = 0
        
        def helper(root):
            if not root:
                return
            nonlocal curr_sum
            helper(root.right)
            temp = root.val
            root.val += curr_sum
            curr_sum += temp
            helper(root.left)
        
        helper(root)
        return root
        
        