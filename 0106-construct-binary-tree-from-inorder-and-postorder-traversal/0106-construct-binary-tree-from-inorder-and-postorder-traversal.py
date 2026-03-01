# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def solver(inord, postord):
            if not inord and not postord:
                return None
            
            root_val = postord[-1]
            root = TreeNode(root_val)
            index = inord.index(root_val)
            root.left = solver(inord[0:index], postord[0:index])
            root.right = solver(inord[index+1:], postord[index:len(postord)-1])
            return root
        
        res = solver(inorder, postorder)
        return res