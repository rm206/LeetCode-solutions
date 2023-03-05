class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l, r = 0, 0 + l1 - 1
        while r < len(s2):
            if tuple(sorted(s1)) == tuple(sorted(s2[l:r+1])):
                return True
            l += 1
            r += 1
        return False