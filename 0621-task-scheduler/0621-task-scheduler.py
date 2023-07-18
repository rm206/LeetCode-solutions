from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]

        heapq.heapify(max_heap)

        q = deque() # [count, time_when_available]
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                new_cnt = 1 + heapq.heappop(max_heap)
                if new_cnt != 0:
                    q.append([new_cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time