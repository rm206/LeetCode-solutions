class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l, r = 0, minutes - 1
        l_res, r_res = l, r
        greatest = -math.inf

        while r < len(customers):
            # curr_sum = sum(customers[l : r + 1])
            curr_sum = sum([customers[i] if grumpy[i]==1 else 0 for i in range(l, r + 1)])

            if curr_sum >= greatest:
                l_res, r_res = l, r
                greatest = curr_sum
            
            l += 1
            r += 1
        
        for i in range(l_res, r_res + 1):
            grumpy[i] = 0
        
        res = 0
        for i in range(len(customers)):
            res += customers[i] if grumpy[i] == 0 else 0
        
        return res