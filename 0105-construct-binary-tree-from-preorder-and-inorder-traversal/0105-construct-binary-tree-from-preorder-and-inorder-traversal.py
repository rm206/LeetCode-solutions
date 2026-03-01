# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def solver(inord, preord):
            if not inord and not preord:
                return None
            
            root_val = preord[0]
            root = TreeNode(root_val)
            index = inord.index(root_val)
            root.left = solver(inord[0:index], preord[1:index+1])
            root.right = solver(inord[index+1:], preord[index+1:])
            return root
        
        res = solver(inorder, preorder)
        return res