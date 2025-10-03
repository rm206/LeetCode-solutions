class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for i in intervals:
            if not stack:
                stack.append(i)
            
            elif stack[-1][1] >= i[0]:
                t0, t1 = stack.pop()
                merge_s, merge_e = min(t0, i[0]), max(t1, i[1])
                stack.append([merge_s, merge_e])
            
            else:
                stack.append(i)
        
        return stack