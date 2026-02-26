# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res
            
        q = []
        q.append(root)
        direc = 1
        while q:
            level = []
            n = len(q)
            for _ in range(n):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if direc == -1:
                level = level[::-1]
            res.append(level)
            direc *= -1
        
        return res