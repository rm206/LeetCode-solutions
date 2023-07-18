import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.curr_median = None

    def addNum(self, num: int) -> None:
        len_max_heap = len(self.max_heap)
        len_min_heap = len(self.min_heap)

        # both the heaps are the same size, both can be empty too
        if len_max_heap == len_min_heap:
            if len_max_heap == 0:
                heapq.heappush(self.min_heap, num)
                self.curr_median = num
            else:
                if num < self.curr_median:
                    heapq.heappush(self.max_heap, -1 * num)
                else:
                    heapq.heappush(self.min_heap, num)
        
        # if the max heap is bigger 2 cases - elt > median and elt < median
        elif len_max_heap > len_min_heap:
            if num > self.curr_median:
                heapq.heappush(self.min_heap, num)
            else:
                transfer = -1 * heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, transfer)
                heapq.heappush(self.max_heap, -1 * num)
        
        # min heap > max heap
        else:
            if num < self.curr_median:
                heapq.heappush(self.max_heap, -1 * num)
            else:
                transfer = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -1 * transfer)
                heapq.heappush(self.min_heap, num)
        
        # update the median
        if len(self.max_heap) > len(self.min_heap):
            self.curr_median = -1 * self.max_heap[0]
        
        elif len(self.min_heap) > len(self.max_heap):
            self.curr_median = self.min_heap[0]
        
        elif len(self.min_heap) == len(self.max_heap):
            self.curr_median = ((-1 * self.max_heap[0]) + self.min_heap[0])/2

    def findMedian(self) -> float:
        return self.curr_median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()