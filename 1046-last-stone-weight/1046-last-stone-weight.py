import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        ctr = 0
        for i, s in enumerate(stones):
            heapq.heappush(heap, (-s, ctr))
            ctr += 1
        
        while len(heap) > 1:
            y, _ = heapq.heappop(heap)
            x, _ = heapq.heappop(heap)
            x *= -1
            y *= -1
            if x == y:
                pass
            else:
                heapq.heappush(heap, (-(y-x), ctr))
                ctr += 1
        
        if not heap:
            return 0
        return -heap[0][0]