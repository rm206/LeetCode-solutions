class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = {}

        for n1, n2 in edges:
            d[n1] = 1 + d.get(n1, 0)
            d[n2] = 1 + d.get(n2, 0)
        
        n = len(d)
        for k, v in d.items():
            if v == n - 1:
                return k