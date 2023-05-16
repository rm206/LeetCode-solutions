class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS = [0] * 26
        arrT = [0] * 26
        
        for c in s:
            arrS[ord(c) - ord('a')] += 1
        for c in t:
            arrT[ord(c) - ord('a')] += 1
        
        for c in s:
            arrT[ord(c) - ord('a')] -= 1
        
        for n in arrT:
            if n != 0:
                return False
        
        return True
        