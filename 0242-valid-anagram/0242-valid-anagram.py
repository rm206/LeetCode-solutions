class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrS = [0] * 26
        arrT = [0] * 26
        
        for c in s: # O(m)
            arrS[ord(c) - ord('a')] += 1
        for c in t: # O(n)
            arrT[ord(c) - ord('a')] += 1
        
        for c in s: # O(m)
            arrT[ord(c) - ord('a')] -= 1
        
        for n in arrT: # O(26)
            if n != 0:
                return False
        
        return True
        