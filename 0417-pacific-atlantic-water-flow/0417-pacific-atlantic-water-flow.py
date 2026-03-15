class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def is_safe(prev_i, prev_j, new_i, new_j, visited):
            return (
                new_i >= 0 and
                new_i < ROWS and
                new_j >= 0 and
                new_j < COLS and
                (new_i, new_j) not in visited and
                heights[prev_i][prev_j] <= heights[new_i][new_j]
            )
        
        def dfs(r, c, visited):
            visited.add((r, c))

            for dx, dy in dirs:
                new_r, new_c = r+dx, c+dy
                if is_safe(r, c, new_r, new_c, visited):
                    dfs(new_r, new_c, visited)
        
        pac, atl = set(), set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for c in range(COLS):
            dfs(0, c, pac)
            dfs(ROWS-1, c, atl)
        for r in range(ROWS):
            dfs(r, 0, pac)
            dfs(r, COLS-1, atl)
        
        res = []

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res