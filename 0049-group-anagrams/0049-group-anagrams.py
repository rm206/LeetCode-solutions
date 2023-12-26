from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        
        res = []
        for v in groups.values():
            res.append(v)
        
        return res