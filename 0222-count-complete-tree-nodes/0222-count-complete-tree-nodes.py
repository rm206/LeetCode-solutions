# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            lh, rh = 1, 1
            curr = node
            while curr.left:
                lh += 1
                curr = curr.left
            curr = node
            while curr.right:
                rh += 1
                curr = curr.right
            
            if lh == rh:
                return (2**lh - 1)
            
            return 1 + dfs(node.left) + dfs(node.right)
        
        return dfs(root)