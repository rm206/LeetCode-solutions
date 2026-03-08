class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for new_s, new_e in intervals:
            to_append_1, to_append_2 = None, None

            if not stack:
                to_append_1, to_append_2 = new_s, new_e
            else:
                if stack[-1][0] <= new_s <= stack[-1][1]:
                    pop_s, pop_e = stack.pop()
                    to_append_1, to_append_2 = min(pop_s, new_s), max(pop_e, new_e)
                else:
                    to_append_1, to_append_2 = new_s, new_e
            
            stack.append([to_append_1, to_append_2])
        
        return stack