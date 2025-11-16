class Solution:
    def numSub(self, s: str) -> int:
        def find_se(i):
            j = i
            while j < len(s)-1 and s[j+1] == "1":
                j += 1
            return i, j

        res = 0
        i = 0
        while i < len(s):
            if s[i] == "1":
                st, e = find_se(i)
                n = e-st+1
                res += (n * (n+1))//2
                i = e + 1
            else:
                i += 1
        
        return res