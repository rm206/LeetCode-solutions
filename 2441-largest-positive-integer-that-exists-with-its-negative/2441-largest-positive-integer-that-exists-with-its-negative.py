class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        res = -1

        for n in nums:
            if n < 0:
                s.add(n)

        for n in nums:
            if (n > 0) and (-n in s) and (n > res):
                res = n
        
        return res