class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        for i, n in enumerate(nums1):
            hmap[n] = i
        
        stack = []
        for i, n in enumerate(nums2):
            while stack and n > stack[-1][0]:
                val, index = stack.pop()
                if index is not None:
                    nums1[index] = n
            
            stack.append([n, hmap.get(n, None)])
        
        while stack:
            val, index = stack.pop()
            if index is not None:
                nums1[index] = -1
        
        return nums1