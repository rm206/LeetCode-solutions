class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Jan 15
        numsDict = {}
        for num in nums:
            numsDict[num] = numsDict.get(num, 0) + 1

        newNumsDict = [[] for i in range(len(nums) + 1)]
        for key,v in numsDict.items():
            newNumsDict[v].append(key)

        res = []
        for i in range(len(newNumsDict) - 1, -1, -1):
            for n in newNumsDict[i]:
                res.append(n)
                if len(res) == k:
                    return res


'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        builder = {}
        for curr in nums:
            builder[curr] = builder.get(curr, 0) + 1
        
        newbuilder = {}
        for key, v in builder.items():
            if v not in newbuilder:
                newbuilder[v] = [key]
            else:
                newbuilder[v].append(key)
        
        res = []
        rescounter = 0
        while rescounter < k:
            temp = max(newbuilder.keys())
            for curr in newbuilder[temp]:
                res.append(curr)
                if len(res) == k:
                    return res
                rescounter += 1
            newbuilder.pop(temp)
            
        return res
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Jan 15
        numsDict = {}
        for num in nums:
            numsDict[num] = numsDict.get(num, 0) + 1

        newNumsDict = [[] for i in range(len(nums) + 1)]
        for key,v in numsDict.items():
            newNumsDict[v].append(key)

        res = []
        for i in range(len(newNumsDict) - 1, -1, -1):
            for n in newNumsDict[i]:
                res.append(n)
                if len(res) == k:
                    return res
'''