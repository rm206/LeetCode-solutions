# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q = []
        parent = {}
        q.append(root)
        while q:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
                parent[node.left] = node
            if node.right:
                q.append(node.right)
                parent[node.right] = node
        
        visited = set()
        q = []
        res = []
        q.append((target, 0))
        while q:
            node, dist_from_target = q.pop(0)
            if node in visited:
                continue

            visited.add(node)
            
            if dist_from_target > k:
                break
            if dist_from_target == k:
                res.append(node.val)
            
            if node in parent:
                q.append((parent[node], dist_from_target+1))
            if node.left:
                q.append((node.left, dist_from_target+1))
            if node.right:
                q.append((node.right, dist_from_target+1))
        
        return res
            