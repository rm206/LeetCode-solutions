import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        
        res = []
        for t in d:
            res.append(d[t])
        
        return res