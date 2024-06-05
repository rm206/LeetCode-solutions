from collections import defaultdict
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = defaultdict(list)
        n = len(words)
        for i in range(ord('a'), ord('z') + 1):
            d[chr(i)] = [0] * n
        
        for i, s in enumerate(words):
            for c in s:
                d[c][i] = 1 + d[c][i]
        
        res = []
        for k, v in d.items():
            for _ in range(min(v)):
                res.append(k)
        
        return res