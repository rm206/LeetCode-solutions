class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        cookie_ptr = len(s) - 1
        ctr = 0
        for i in range(len(g)-1, -1, -1):
            if cookie_ptr < 0:
                break
            if g[i] <= s[cookie_ptr]:
                ctr += 1
                cookie_ptr -= 1
        
        return ctr