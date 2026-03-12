class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]

        for key, val in c.items():
            freq[val].append(key)
        
        res = []
        for arr in freq[::-1]:
            for el in arr:
                if k:
                    res.append(el)
                    k -= 1
        
        return res
