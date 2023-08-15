# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def solver(preorder, inorder):
            # base case
            if not preorder or not inorder:
                return None
            
            root = TreeNode(preorder[0])
            index = inorder.index(root.val)
            root.left = solver(preorder[1 : index + 1], inorder[ : index])
            root.right = solver(preorder[index + 1 : ], inorder[index + 1 : ])
            
            return root
        
        res = solver(preorder, inorder)
        return res