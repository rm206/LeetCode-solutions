class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        c = set(nums)

        while original in c:
            original *= 2
        
        return original