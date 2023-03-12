class Solution:
    def find_row(self, matrix, rows, cols, target):
        row_l, row_r = 0, rows - 1
        while row_l <= row_r:
            mid = (row_l + row_r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][cols-1]:
                return mid
            elif matrix[mid][0] > target:
                row_r = mid - 1
            else:
                row_l = mid + 1
        
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[ROWS-1][COLS-1]:
            return False
        
        row = self.find_row(matrix, ROWS, COLS, target)
        if row == -1:
            return False
        
        col_l, col_r = 0, COLS - 1
        while col_l <= col_r:
            mid = (col_l + col_r)//2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                col_r = mid - 1
            else:
                col_l = mid + 1
        
        return False
        