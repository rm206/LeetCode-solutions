"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if not node.neighbors:
            return Node(node.val)
            
        def dfs(curr):
            visited.add(curr)
            mp[curr] = Node(curr.val)

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

        visited = set()
        mp = {}
        dfs(node)

        for orig, cpy in mp.items():
            for neighbor in orig.neighbors:
                mp[orig].neighbors.append(mp[neighbor])
        
        return mp[node]