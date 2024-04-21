from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def builder():
            d = defaultdict(list)
            for u, v in edges:
                d[u].append(v)
                d[v].append(u)
            return d
        
        graph = builder()
        q = []
        q.append(source)
        found = False
        close = set()
        
        while q:
            node = q.pop(0)
            if node in close:
                continue
            close.add(node)
            if node == destination:
                found = True
                break
            for neigh in graph[node]:
                q.append(neigh)
        
        return found