class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        merged_s = newInterval[0]
        merged_e = newInterval[1]
        while i < n and intervals[i][0] <= newInterval[1]:
            merged_s = min(merged_s, intervals[i][0])
            merged_e = max(merged_e, intervals[i][1])
            i += 1
        
        res.append([merged_s, merged_e])

        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res