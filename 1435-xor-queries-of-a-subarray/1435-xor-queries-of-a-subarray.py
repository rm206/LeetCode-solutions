class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        curr = 0
        pref = []

        for n in arr:
            curr = curr ^ n
            pref.append(curr)
        
        res = []

        for left, right in queries:
            if left > 0:
                res.append(pref[right] ^ pref[left - 1])
            else:
                res.append(pref[right])
        
        return res