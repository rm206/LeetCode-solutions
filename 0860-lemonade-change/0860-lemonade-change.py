class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {
            5  : 0,
            10 : 0,
            20 : 0
        }

        for b in bills:
            if b == 5:
                d[5] += 1
            
            elif b == 10:
                if d[5] >= 1:
                    d[5] -= 1
                    d[10] += 1
                else:
                    return False
            
            else:
                if d[5] >= 1 and d[10] >= 1:
                    d[5] -= 1
                    d[10] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return False
                d[20] += 1
        
        return True