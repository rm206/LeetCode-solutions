class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)

        total_sum = 0
        seen = set()
        double_val = None

        for i in range(len(grid)):
            for j in range(len(grid)):
                elt = grid[i][j]
                total_sum += elt
                if elt in seen:
                    double_val = grid[i][j]
                seen.add(elt)
        
        total_els = n * n
        diff = ((total_els * (total_els + 1))//2) - total_sum
        
        if double_val + diff < n*n + 1 and double_val + diff not in seen:
            missing = double_val + diff
        else:
            missing = double_val - diff
        
        return [double_val, missing]