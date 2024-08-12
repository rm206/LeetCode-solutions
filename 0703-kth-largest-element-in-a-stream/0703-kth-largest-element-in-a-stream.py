import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.seen = set()
        self.heap = []
        self.heap_len = 0
        self.k = k

        for n in nums:
            heapq.heappush(self.heap, n)
            self.heap_len += 1
            
            if self.heap_len > self.k:
                heapq.heappop(self.heap)
                self.heap_len -= 1

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.heap_len += 1

        if self.heap_len > self.k:
            heapq.heappop(self.heap)
            self.heap_len -= 1
        
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)