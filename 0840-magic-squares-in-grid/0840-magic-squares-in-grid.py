"""
mg = magic grids

grid may be smaller than 3x3 -> 0 mg

mg must be contiguous
    - map which is added to and removeed
        - col by col
        - row by row

find sum of all rows, all cols, 2 diagonals

if any cell == 0 or any cell > 9, not mg
duplicate -> not mg
"""

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(row, col):
            s = set()
            for i in range(3):
                for j in range(3):
                    s.add(grid[row+i][col+j])
            if not (s == set(range(1, 10))):
                return False
            
            vals = []

            vals.append(grid[row+0][col]+grid[row+0][col+1]+grid[row+0][col+2])
            vals.append(grid[row+1][col]+grid[row+1][col+1]+grid[row+1][col+2])
            vals.append(grid[row+2][col]+grid[row+2][col+1]+grid[row+2][col+2])

            vals.append(grid[row+0][col+0]+grid[row+1][col+0]+grid[row+2][col+0])
            vals.append(grid[row+0][col+1]+grid[row+1][col+1]+grid[row+2][col+1])
            vals.append(grid[row+0][col+2]+grid[row+1][col+2]+grid[row+2][col+2])

            vals.append(grid[row+0][col+0]+grid[row+1][col+1]+grid[row+2][col+2])
            vals.append(grid[row+0][col+2]+grid[row+1][col+1]+grid[row+2][col+0])

            return all(map(lambda x: x == 15, vals))

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m - 2):
            for j in range(n - 2):
                if is_magic(i, j):
                    res += 1
        
        return res
        