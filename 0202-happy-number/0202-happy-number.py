"""
seen = set()
        while True:
            s = sum(list(map(lambda x: int(x)**2, list(str(n)))))
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
            n = s
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_square_digit(num):
            return sum(list(map(lambda x: int(x)**2, list(str(num)))))
        
        slow, fast = n, n
        while True:
            slow = sum_square_digit(slow)
            fast = sum_square_digit(sum_square_digit(fast))
            if slow == fast:
                break
        
        return slow == 1