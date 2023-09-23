from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        d = Counter(s)
        heap = [[-cnt, char] for char, cnt in d.items()]
        heapq.heapify(heap)
        
        cnt, char = heapq.heappop(heap)
        cnt *= -1
        
        res = [None for _ in range(len(s))]
        
        if cnt > (len(s) + 1) // 2:
            return ""
        
        i = 0
        while cnt:
            res[i] = char
            i += 2
            cnt -= 1
        

        while heap:
            cnt, char = heapq.heappop(heap)
            cnt *= -1
            while cnt:
                if i >= len(s):
                    i = 1
                    
                res[i] = char
                i += 2
                cnt -= 1
        
        res = "".join(res)
        return res
                

'''
d = Counter(s)
heap = [[-cnt, char] for char, cnt in d.items()]
heapq.heapify(heap)

prev = None
res = []

while heap or prev:

    if prev and not heap:
        print("in")
        return ""

    cnt, char = heapq.heappop(heap)
    res.append(char)
    cnt += 1

    if prev:
        heapq.heappush(heap, prev)
        prev = None

    if cnt != 0:
        prev = [cnt, char]

res = "".join(res)
print(res)
return res
'''