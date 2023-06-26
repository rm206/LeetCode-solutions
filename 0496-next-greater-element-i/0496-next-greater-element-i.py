class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for i in nums2:
            mapping[i] = -1

        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                val = stack.pop()
                mapping[val] = i
            stack.append(i)
        
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            res[i] = mapping[nums1[i]] 
        
        return res