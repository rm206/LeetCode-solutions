class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        p1, p2 = 0, 0

        while p1 < len(v1) or p2 < len(v2):
            val1 = int(v1[p1]) if p1 < len(v1) else 0
            val2 = int(v2[p2]) if p2 < len(v2) else 0
            
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
            else:
                p1 += 1
                p2 += 1
        
        return 0