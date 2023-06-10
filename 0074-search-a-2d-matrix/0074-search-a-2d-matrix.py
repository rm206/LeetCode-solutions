class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findrow(m: int, n: int):
            top, bottom = 0, m - 1
            while top <= bottom:
                mid = (top + bottom) // 2
                
                if matrix[mid][0] <= target and target <= matrix[mid][n - 1]:
                    return mid
                
                elif target < matrix[mid][0]:
                    bottom = mid - 1
                
                else:
                    top = mid + 1
            
            return -1
        
        # find row to which the target belongs (use findrow)
        # with the row, run the regular binary search
        m, n = len(matrix), len(matrix[0])
        target_row = findrow(m, n)
        
        if target_row == -1:
            return False
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            
            if matrix[target_row][mid] == target:
                return True
            
            elif target < matrix[target_row][mid]:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return False
        
        
        