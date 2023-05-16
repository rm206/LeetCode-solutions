class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        initMap = {}
        for n in nums:
            initMap[n] = 1 + initMap.get(n, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for key,v in initMap.items():
            freq[v].append(key)        

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                