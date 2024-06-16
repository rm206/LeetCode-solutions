import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_heap = []
        for i in range(len(profits)):
            heapq.heappush(capital_heap, [capital[i], profits[i]])
        profit_heap = []

        while k > 0:
            while capital_heap and capital_heap[0][0] <= w:
                _, p = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap, -p)
            
            if not profit_heap:
                break
            
            w += -1 * heapq.heappop(profit_heap)
            k -= 1
        
        return w

        """
        builder = [[capital[i], profits[i]] for i in range(len(profits))]
        builder.sort(key = lambda x : (-x[1], x[0]))
        used = [False] * len(builder)

        while k > 0:
            for i in range(len(builder)):
                if not used[i] and builder[i][0] <= w:
                    w = w + builder[i][1]
                    k -= 1
                    break
        
        return w
        """