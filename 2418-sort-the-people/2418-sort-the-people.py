import heapq
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # heap = []
        # for name, ht in zip(names, heights):
        #     heapq.heappush(heap, [-ht, name])
        
        # res = []
        # while heap:
        #     ht, name = heapq.heappop(heap)
        #     res.append(name)
        
        # return res
        temp = []
        for name, ht in zip(names, heights):
            temp.append([ht, name])
        
        temp.sort(reverse=True)

        res = []
        for ht, name in temp:
            res.append(name)
        
        return res