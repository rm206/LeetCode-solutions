class StockSpanner:

    def __init__(self):
        self.day = 0
        self.stack = []

    def next(self, price: int) -> int:
        index = -1
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        
        if self.stack:
            index = self.stack[-1][0]

        self.stack.append([self.day, price])
        today = self.day
        self.day += 1

        return today-index


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)