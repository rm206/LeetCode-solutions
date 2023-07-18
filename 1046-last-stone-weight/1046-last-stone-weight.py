import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            w1 = -1 * heapq.heappop(stones)
            w2 = -1 * heapq.heappop(stones)

            if w1 != w2:
                heapq.heappush(stones, -1 * abs(w1 - w2))
            
        stones.append(0)
        return -1 * stones[0]