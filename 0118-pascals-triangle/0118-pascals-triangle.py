class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            temp = [0] + res[-1] + [0]
            prev = 0
            curr = 1
            to_add = []
            while prev <= i:
                to_add.append(temp[prev] + temp[curr])
                prev += 1
                curr += 1
            res.append(to_add)
        
        return res
