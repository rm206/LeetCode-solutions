class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N, M = len(rowSum), len(colSum)
        res = [[0 for i in range(M)] for j in range(N)] 

        for r in range(N):
            res[r][0] = rowSum[r]
        
        for c in range(M):
            curr_sum = sum([res[r][c] for r in range(N)])
            
            r = 0
            while curr_sum > colSum[c]:
                diff = curr_sum - colSum[c]
                to_shift = min(diff, res[r][c])
                res[r][c] -= to_shift
                res[r][c+1] += to_shift
                curr_sum -= to_shift
                r += 1
        
        return res