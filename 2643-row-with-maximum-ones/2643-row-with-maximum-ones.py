class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = None
        max_ones_found = -1

        for i, row in enumerate(mat):
            if sum(row) > max_ones_found:
                res = i
                max_ones_found = sum(row)
        
        return [res, max_ones_found]