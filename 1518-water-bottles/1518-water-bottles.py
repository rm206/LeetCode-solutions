class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        full = numBottles
        res = 0

        while True:
            res += full
            empty += full
            full = 0

            full += empty // numExchange
            empty = empty % numExchange

            if full == 0:
                break

        return res