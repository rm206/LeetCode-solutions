class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        build = defaultdict(list)
        
        for s in strs:
            build[tuple(sorted(s))].append(s)
        
        res = []
        for key, val in build.items():
            temp = []
            for v in val:
                temp.append(v)
            res.append(temp)
        
        return res