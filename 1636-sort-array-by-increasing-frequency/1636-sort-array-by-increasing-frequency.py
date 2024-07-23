import heapq
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = {}

        for n in nums:
            c[n] = 1 + c.get(n, 0)
        
        # temp = []
        # for k, v in c.items():
        #     temp.append([v, k])
        
        # temp.sort(key=lambda x: (x[0], -x[1]))
        # j = 0
        # i = 0

        # while j < len(temp):
        #     freq, val = temp[j]            
        #     for _ in range(freq):
        #         nums[i] = val
        #         i += 1
        #     j += 1
        
        heap = []
        for k, v in c.items():
            heapq.heappush(heap, [v, -k])
        
        i = 0
        while heap:
            iters, val = heapq.heappop(heap)
            val *= -1
            for _ in range(iters):
                nums[i] = val
                i += 1
        
        return nums