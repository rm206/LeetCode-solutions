class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def is_not_paired(index):
            return (index == 0 and nums[index] != nums[index+1]) or (index == n-1 and nums[index] != nums[index-1]) or (nums[index-1] != nums[index] and nums[index] != nums[index+1])

        n = len(nums)

        if n == 1:
            return nums[0]

        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2

            if is_not_paired(m):
                return nums[m]
            
            elif (m > 0 and nums[m-1] == nums[m]) :
                if (m-l+1) %2 == 0:
                    l = m + 1
                else:
                    r = m - 2
            
            else:
                if (r-m+1) % 2 == 0:
                    r = m - 1
                else:
                    l = m + 2