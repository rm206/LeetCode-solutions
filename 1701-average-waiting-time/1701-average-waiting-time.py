class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = customers[0][0]
        s = 0
        for start, wait in customers:
            if start > curr_time:
                s += wait
                curr_time = start + wait
            else:
                s += (curr_time + wait) - start
                curr_time += wait
        
        return s / len(customers)