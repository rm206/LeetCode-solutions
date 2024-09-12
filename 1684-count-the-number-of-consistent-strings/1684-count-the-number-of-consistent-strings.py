class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0

        for w in words:
            if set(w) == (set(w) & set(allowed)):
                res += 1
        
        return res