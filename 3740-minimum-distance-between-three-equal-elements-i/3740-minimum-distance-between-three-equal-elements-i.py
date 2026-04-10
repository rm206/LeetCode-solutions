class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        d = defaultdict(list)

        for i, n in enumerate(nums):
            d[n].append(i)
        
        res = None

        for k, v in d.items():
            if len(v) >= 3:
                temp = math.inf
                for a in range(0, len(v)):
                    for b in range(a+1, len(v)):
                        for c in range(b+1, len(v)):
                            temp = min(temp, (v[b]-v[a])+(v[c]-v[b])+(v[c]-v[a]))
                res = temp if res is None else min(res, temp)
        
        return res if res is not None else -1