class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Nov 27
        # O(m * nlogn)
#         builder = {}
#         for curr in strs:
#             temp = tuple(sorted(curr))
#             if temp not in builder:
#                 builder[temp] = [curr]
#             else:
#                 builder[temp].append(curr)
        
#         res = []
#         for curr in builder:
#             res.append(builder[curr])
        
#         return res
        
        # O(m * n)
        # builder = {}
        # for curr in strs:
        #     temp = [0] * 26
        #     for c in curr:
        #         temp[ord(c) - ord('a')] += 1
        #     temp = tuple(temp)
            
        #     if temp not in builder:
        #         builder[temp] = [curr]
        #     else:
        #         builder[temp].append(curr)
        
        # res = []
        # for curr in builder:
        #     res.append(builder[curr])
        
        # return res

        # Jan 9
        commonDict = {}
        for curr in strs:
            sortedTupledCurr = tuple(sorted(curr))
            if sortedTupledCurr not in commonDict:
                commonDict[sortedTupledCurr] = [curr]
            else:
                commonDict[sortedTupledCurr].append(curr)
        
        res = []
        for curr in commonDict:
            res.append(commonDict[curr])
        return res