# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_subtree(node1, node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (not node1 and node2):
                return False
            if node1.val == node2.val and check_subtree(node1.left, node2.left) and check_subtree(node1.right, node2.right):
                return True
            else:
                return False
        
        def dfs(node):
            nonlocal subRoot
            if not node:
                return False
            
            if check_subtree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)