from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split())
        s2 = Counter(s2.split())

        res = []

        for word, cnt in s1.items():
            if cnt == 1 and word not in s2:
                res.append(word)
        
        for word, cnt in s2.items():
            if cnt == 1 and word not in s1:
                res.append(word)

        return res