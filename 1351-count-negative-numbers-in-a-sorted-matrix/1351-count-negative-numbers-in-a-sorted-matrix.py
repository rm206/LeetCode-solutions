class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for r in range(m):
            s, e = 0, n - 1
            curr_min = None
            
            while s <= e:
                mid = (s + e) // 2
                
                if grid[r][mid] < 0:
                    curr_min = mid
                    e = mid - 1
                elif grid[r][mid] > 0:
                    s = mid + 1
                else:
                    s = mid + 1
            
            if curr_min is not None:
                res += (n-curr_min)
        
        return res