from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        counts = defaultdict(int)

        for i in range(n):
            for j in range(n):
                counts[grid[i][j]] += 1
        
        for i in range(n*n + 1):
            if counts[i] == 2:
                double_val = i
            if counts[i] == 0:
                missing = i
        
        return [double_val, missing]