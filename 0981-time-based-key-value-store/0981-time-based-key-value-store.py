from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        else:
            search_arr = self.d[key]
            res = -1
            l, r = 0, len(search_arr) - 1
            
            while l <= r:
                mid = (l + r) // 2
                
                if search_arr[mid][0] == timestamp:
                    return search_arr[mid][1]
                
                elif search_arr[mid][0] < timestamp:
                    res = mid
                    l = mid + 1
                
                else:
                    r = mid - 1
            
            if res == -1:
                return ""
            else:
                return search_arr[res][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)