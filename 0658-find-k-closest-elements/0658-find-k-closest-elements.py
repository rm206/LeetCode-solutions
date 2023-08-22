import heapq
from collections import defaultdict

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        min_heap = []
        d = defaultdict(list)
        
        for num in arr:
            heapq.heappush(min_heap, abs(num - x))
            d[abs(num - x)].append(num)
        
        res = []
        visited = set()
        
        while k:
            diff = heapq.heappop(min_heap)
            if diff in visited:
                continue
            visited.add(diff)
            for num in d[diff]:
                if k:
                    res.append(num)
                    k -= 1
        
        res.sort()
        return res