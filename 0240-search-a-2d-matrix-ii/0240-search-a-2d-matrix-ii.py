class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        row, col = 0, n - 1
        
        while row < m and col >= 0:
            
            elt = matrix[row][col]
            
            if elt == target:
                return True
            
            elif elt < target:
                row += 1
            
            else:
                col -= 1
        
        return False