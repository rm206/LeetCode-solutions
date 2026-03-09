from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        chars = Counter(list(s))
        counts = [[] for _ in range(len(s) + 1)]

        for k, v in chars.items():
            counts[v].append(k)
        
        res = []

        for i in range(len(counts)-1, 0, -1):
            for j in counts[i]:
                for _ in range(i):
                    res.append(j)
        
        return "".join(res)