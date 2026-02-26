# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = []
        res = None
        q.append(root)

        while q:
            is_first_el_found = False
            first_el_found = None
            l = len(q)
            for _ in range(l):
                node = q.pop(0)
                if not is_first_el_found:
                    is_first_el_found = True
                    first_el_found = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res = first_el_found
        
        return res