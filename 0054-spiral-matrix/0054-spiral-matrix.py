class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        count = 0
        total = m * n
        
        starting_row = 0
        starting_col = 0
        ending_row = m - 1
        ending_col = n - 1
        
        while count < total:
            # print starting row
            for col in range(starting_row, ending_col + 1):
                if count < total:
                    res.append(matrix[starting_row][col])
                    count += 1
            starting_row += 1
            
            # print ending col
            for row in range(starting_row, ending_row + 1):
                if count < total:
                    res.append(matrix[row][ending_col])
                    count += 1
            ending_col -= 1
            
            # print ending row
            for col in range(ending_col, starting_col -1, -1):
                if count < total:
                    res.append(matrix[ending_row][col])
                    count += 1
            ending_row -= 1
            
            # print starting col
            for row in range(ending_row, starting_row -1, -1):
                if count < total:
                    res.append(matrix[row][starting_col])
                    count += 1
            starting_col += 1
        
        return res