class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for s, e in intervals:
            if not res:
                res.append([s, e])
            else:
                if s <= res[-1][1]:
                    prev = res.pop()
                    to_add = [min(s, prev[0]), max(e, prev[1])]
                else:
                    to_add = [s, e]
                
                res.append(to_add.copy())
        
        return res