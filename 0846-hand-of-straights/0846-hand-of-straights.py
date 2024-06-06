class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        d = {}
        for n in hand:
            d[n] = 1 + d.get(n, 0)
        
        while d:
            val = min(d.keys())
            d[val] -= 1
            if d[val] == 0:
                d.pop(val)
            for i in range(1, groupSize):
                if not d:
                    return False
                if not val + i in d:
                    return False
                d[val+i] -= 1
                if d[val+i] == 0:
                    d.pop(val+i)
        
        return True