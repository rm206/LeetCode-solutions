class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        import heapq
        
        count = Counter(words)
        max_heap = []
        
        for word, freq in count.items():
            heapq.heappush(max_heap, [-1 * freq, word])
        
        res = []
        while k:
            freq, word = heapq.heappop(max_heap)
            res.append(word)
            k -= 1
        
        return res