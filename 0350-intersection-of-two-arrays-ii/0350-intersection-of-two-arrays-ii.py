from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        res = []

        for k, v in d1.items():
            iter_val = min(v, d2.get(k, 0))    
            for _ in range(iter_val):
                res.append(k)
        
        return res