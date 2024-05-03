class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        m, n = len(v1), len(v2)
        i, j = 0, 0

        while i < m or j < n:            
            val1 = int(v1[i]) if i < m else 0
            val2 = int(v2[j]) if j < n else 0
            
            if val1 < val2:
                return -1
            if val1 > val2:
                return 1
            
            i += 1
            j += 1
        
        return 0