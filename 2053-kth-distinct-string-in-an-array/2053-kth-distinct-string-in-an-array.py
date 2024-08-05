from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)

        ctr = 0
        for s in arr:
            if c[s] == 1 and ctr == k - 1:
                return s
            elif c[s] == 1:
                ctr += 1
        
        return ""