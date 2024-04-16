# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        
        q = []
        q.append([root, 1])
        
        while q:
            node, curr_depth = q.pop(0)
            
            if curr_depth == depth - 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
            
            if node.left:
                q.append([node.left, curr_depth + 1])
            if node.right:
                q.append([node.right, curr_depth + 1])
        
        return root