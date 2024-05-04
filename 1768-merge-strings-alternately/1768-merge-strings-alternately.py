class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        turn = 1
        i, j = 0, 0
        res = ""

        while i < len(word1) or j < len(word2):
            v1 = word1[i] if i < len(word1) else ""
            v2 = word2[j] if j < len(word2) else ""

            if turn == 1:
                res += v1
                i += 1
            else:
                res += v2
                j += 1
            
            turn *= -1
        
        return res