class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1
        
        val = time // (n-1)

        if val % 2 == 0:
            return time % (n - 1) + 1
        else:
            return n - (time % (n - 1))