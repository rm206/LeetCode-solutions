import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x_c, y_c):
            return (x_c**2 + y_c**2)
        
        heap = []
        for i, n in enumerate(points):
            x, y = n
            if not heap or len(heap) < k:
                heapq.heappush(heap, (-dist(x, y), i))
            elif dist(x, y) < (-1 * heap[0][0]):
                heapq.heappop(heap)
                heapq.heappush(heap, (-dist(x, y), i))
        
        res = []

        for dist, index in heap:
            res.append(points[index])
        
        return res