class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res = 0
        cnt = 0
        i = len(happiness) - 1
        while cnt < k:
            res += max(0, happiness[i] - cnt)
            cnt += 1
            i -= 1
        
        return res
        '''
        import heapq
        h = []
        i = 0
        k_c = k
        while k:
            heapq.heappush(h, happiness[i])
            i += 1
            k -= 1
        while i < len(happiness):
            if happiness[i] > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, happiness[i])
            i += 1
        
        res = 0
        while k_c:
            res += max(0, heapq.heappop(h) - (k_c - 1))
            k_c -= 1
        
        return res
        '''