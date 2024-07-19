class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r = {}
        c = {}

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                r[row] = min(r.get(row, math.inf), matrix[row][col])
                c[col] = max(c.get(col, -math.inf), matrix[row][col])
        
        return list(set(r.values()) & set(c.values()))