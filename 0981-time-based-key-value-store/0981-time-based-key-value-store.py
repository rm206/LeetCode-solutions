import collections
class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.store.get(key, [])
        
        # find ans
        l, r = 0, len(vals) - 1
        while l <= r:
            mid = (l + r) // 2
            
            if timestamp == vals[mid][0]:
                return vals[mid][1]
            
            elif vals[mid][0] < timestamp:
                res = vals[mid][1]
                l = mid + 1
            
            else:
                r = mid - 1
    
        return res
        
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)