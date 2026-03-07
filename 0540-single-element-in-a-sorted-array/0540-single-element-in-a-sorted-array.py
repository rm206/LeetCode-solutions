class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2

            if (m > 0 and m<n-1 and nums[m-1] != nums[m] and nums[m] != nums[m+1]) or (m == 0 and nums[m] != nums[m+1]) or (m == n-1 and nums[m] != nums[m-1]):
                return nums[m]
            
            elif (m > 0 and nums[m-1] == nums[m]) :
                if (m-l+1) %2 != 0:
                    r = m - 2
                else:
                    l = m + 1
            
            else:
                if (r-m+1) % 2 == 0:
                    r = m - 1
                else:
                    l = m + 2