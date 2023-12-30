class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t = []
        for i in range(m):
            t.append(nums1[i])
            nums1[i] = 0
        
        p1, p2 = 0, 0
        p = 0
        
        while p < m + n:
            val1 = t[p1] if p1 < m else float('inf')
            val2 = nums2[p2] if p2 < n else float('inf')
            
            if val1 < val2:
                nums1[p] = val1
                p1 += 1
            else:
                nums1[p] = val2
                p2 += 1
            
            p += 1