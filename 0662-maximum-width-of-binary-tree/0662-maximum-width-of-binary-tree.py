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
            l = len(q)
            _, first_index = q[0]
            for i in range(l):
                node, index = q.pop(0)

                if i == l-1:
                    res = max(res, index-first_index+1)
                
                if node.left:
                    q.append((node.left, 2*(index - first_index)))
                if node.right:
                    q.append((node.right, 2*(index - first_index)+1))
        
        return res