class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for n in nums2:
            d[n] = -1

        for i, n in enumerate(nums2):
            if not stack:
                stack.append(n)
            else:
                while stack and n > stack[-1]:
                    val = stack.pop()
                    d[val] = n
                stack.append(n)
        
        res = []
        for n in nums1:
            res.append(d[n])
        
        return res