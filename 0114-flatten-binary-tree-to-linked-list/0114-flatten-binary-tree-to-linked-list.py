# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            if not node:
                return
            inord.append(node)
            inorder(node.left)
            inorder(node.right)
        
        inord = []
        inorder(root)
        inord.append(None)

        for i in range(len(inord)-1):
            inord[i].left = None
            inord[i].right = inord[i+1]
        
        return inord[0]