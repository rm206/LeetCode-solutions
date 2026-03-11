"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def preord(node):
            if not node:
                return
            res.append(node.val)
            for ch in node.children:
                preord(ch)

        res = []
        preord(root)
        return res