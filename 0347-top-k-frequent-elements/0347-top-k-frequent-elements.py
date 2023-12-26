import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        cnt = Counter(nums)
        for key in cnt:
            heapq.heappush(arr, [-1 * cnt[key], key])
        
        res = []
        while k > 0:
            freq, val = heapq.heappop(arr)
            res.append(val)
            k -= 1
        
        return res