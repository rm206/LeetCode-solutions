from collections import Counter
import heapq

class Solution:
    def minimumPushes(self, word: str) -> int:
        d = Counter(word)
        heap = []

        for k, v in d.items():
            heapq.heappush(heap, -v)
        ctr = 0

        res = 0
        while heap:
            freq = heapq.heappop(heap)
            freq *= -1
            res += freq * (ctr//8+1)
            ctr += 1
        
        return res