import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        ugly_numbers_pot = []
        seen = set()

        heapq.heappush(ugly_numbers_pot, 1)
        seen.add(1)

        current_ugly = 1

        for i in range(n):
            current_ugly = heapq.heappop(ugly_numbers_pot)

            if current_ugly * 2 not in seen:
                heapq.heappush(ugly_numbers_pot, current_ugly * 2)
                seen.add(current_ugly * 2)
            if current_ugly * 3 not in seen:
                heapq.heappush(ugly_numbers_pot, current_ugly * 3)
                seen.add(current_ugly * 3)
            if current_ugly * 5 not in seen:
                heapq.heappush(ugly_numbers_pot, current_ugly * 5)
                seen.add(current_ugly * 5)

        return current_ugly
        

"""
def is_ugly(n: int) -> bool:
    if n <= 0:
        return False
    
    if 1 <= n <= 3:
        return True
    
    while n % 2 == 0:
        n = n // 2
    
    while n % 3 == 0:
        n = n // 3
    
    while n % 5 == 0:
        n = n // 5
    
    return n == 1

if n <= 6:
    return n

ctr = 6
num = 7
while True:
    if is_ugly(num):
        ctr += 1
    
    if ctr == n:
        return num
    
    num += 1
"""