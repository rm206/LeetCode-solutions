import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        i = 0
        while i < k:
            heapq.heappush(min_heap, nums[i])
            i += 1
        
        for j in range(i, len(nums)):
            if nums[j] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[j])
        
        return min_heap[0]