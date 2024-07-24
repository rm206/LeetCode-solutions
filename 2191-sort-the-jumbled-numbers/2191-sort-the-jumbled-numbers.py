import heapq
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            return int(''.join(map(lambda x: str(mapping[int(x)]), str(num))))
        
        heap = []
        for i, n in enumerate(nums):
            heapq.heappush(heap, [convert(n), i, n])
        
        for i in range(len(nums)):
            _, _, val = heapq.heappop(heap)
            nums[i] = val
        
        return nums
