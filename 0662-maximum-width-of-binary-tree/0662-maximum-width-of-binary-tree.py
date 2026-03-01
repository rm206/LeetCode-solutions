# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = []
        res = -math.inf
        q.append((root, 1))

        while q:
            level = []
            l = len(q)
            for _ in range(l):
                node, index = q.pop(0)
                level.append((node, index))
                if node.left:
                    q.append((node.left, 2*index))
                if node.right:
                    q.append((node.right, 2*index+1))
            width = level[-1][1]-level[0][1]+1
            res = max(res, width)
        
        return res