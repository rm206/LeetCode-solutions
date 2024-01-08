class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        curr = [1]
        res = [[1]]
        numRows -= 1
        
        while numRows:
            curr = res[-1]
            curr = [0] + curr + [0]
            to_add = []
            for i in range(len(curr) - 1):
                to_add.append(curr[i] + curr[i + 1])
            res.append(to_add)
            numRows -= 1
        
        return res