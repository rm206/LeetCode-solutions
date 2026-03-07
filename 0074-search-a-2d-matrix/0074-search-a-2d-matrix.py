class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            mid = (l + r) // 2
            mid_val = matrix[mid//cols][mid%cols]

            if mid_val == target:
                return True

            if target < mid_val:
                r = mid - 1
            
            else:
                l = mid + 1
        
        return False