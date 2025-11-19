class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        from collections import Counter
        c = Counter(nums)

        while original in c:
            print(original)
            original *= 2
        
        return original