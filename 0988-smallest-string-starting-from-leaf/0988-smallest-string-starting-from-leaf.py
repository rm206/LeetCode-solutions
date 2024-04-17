# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
import copy
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def solver(node, prev):
            nonlocal res
            
            curr = chr(ord('a')+node.val) + prev
            
            if not node.left and not node.right:
                if res == "":
                    res = copy.deepcopy(curr)
                else:
                    if curr < res:
                        res = copy.deepcopy(curr)
                return
            
            if node.left:
                solver(node.left, curr)
            if node.right:
                solver(node.right, curr)
        

        res = ""
        solver(root, "")
        return res