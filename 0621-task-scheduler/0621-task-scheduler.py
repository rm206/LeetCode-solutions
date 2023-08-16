import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # place most occuring tasks first
        # heap can maintain the curr most freq elt
        # q can hold tasks in place
        # global time to check if cooldown period ended
        
        max_heap = []
        q = []
        time = 0
        counts = Counter(tasks)
        
        for task, freq in counts.items():
            heapq.heappush(max_heap, (-1 * freq, task))
        
        while max_heap or q:
            time += 1
            
            if q and q[0][2] == time:
                el = q.pop(0)
                heapq.heappush(max_heap, (-1 * el[0], el[1]))
            
            if max_heap:
                elt = heapq.heappop(max_heap)
                if (elt[0] * -1) - 1 > 0:
                    q.append(((elt[0] * -1) - 1, elt[1], time + n + 1))
            
            
        
        return time