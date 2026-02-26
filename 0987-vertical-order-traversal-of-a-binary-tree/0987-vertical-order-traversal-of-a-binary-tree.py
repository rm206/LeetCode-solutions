# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
import heapq
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        q = []
        q.append((root, 0, 0))

        while q:
            node, row, col = q.pop(0)
            hashmap[col].append((row, node.val))
            if node.left:
                q.append((node.left, row+1, col-1))
            if node.right:
                q.append((node.right, row+1, col+1))
        
        res = []
        while hashmap:
            val = min(hashmap)
            res.append(list(map(lambda x: x[1], sorted(hashmap[val]))))
            del(hashmap[val])
        
        return res