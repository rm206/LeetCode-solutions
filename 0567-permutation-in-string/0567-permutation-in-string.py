class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = [0] * 26
        for c in s1:
            d1[ord(c) - ord('a')] += 1

        d2 = [0] * 26
        l, r = 0, 0

        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                d2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            d2[ord(s2[r]) - ord('a')] += 1

            if d1 == d2:
                return True
            
        
        return False