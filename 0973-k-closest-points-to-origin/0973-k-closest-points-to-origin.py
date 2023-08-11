import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        for i in range(len(points)):
            dist = math.sqrt(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(min_heap, (dist, [points[i][0], points[i][1]]))
        
        res = []
        while k:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1
        
        return res