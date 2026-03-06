class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        builder_ptr = m+n-1
        p1, p2 = m-1, n-1

        while p1 > -1 or p2 > -1:
            val1 = nums1[p1] if p1 >= 0 else -math.inf
            val2 = nums2[p2] if p2 >= 0 else -math.inf

            if val1 >= val2:
                nums1[builder_ptr] = val1
                p1 -=1
                
            else:
                nums1[builder_ptr] = val2
                p2 -=1
            
            builder_ptr -= 1