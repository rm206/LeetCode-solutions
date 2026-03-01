class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            s = sum(list(map(lambda x: int(x)**2, list(str(n)))))
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
            n = s