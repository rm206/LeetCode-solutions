from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntrs = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in cntrs.items():
            freq[c].append(n)
        
        print(freq)
        res = []

        for curr_arr in freq[::-1]:
            for n in curr_arr:
                if k > 0:
                    res.append(n)
                    k -= 1
        
        return res