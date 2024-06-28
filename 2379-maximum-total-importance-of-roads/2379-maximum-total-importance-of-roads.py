import heapq

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = {}
        for e1, e2 in roads:
            d[e1] = 1 + d.get(e1, 0)
            d[e2] = 1 + d.get(e2, 0)
        
        heap = []
        for k, v in d.items():
            heapq.heappush(heap, [-v, k])
        
        d = {}
        while n and heap:
            degree, node = heapq.heappop(heap)
            d[node] = n
            n -= 1
        
        res = 0
        for e1, e2 in roads:
            res += (d[e1] + d[e2])
        
        return res