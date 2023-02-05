class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Nov 25
        # s = set({})
        # for curr in nums:
        #     if curr in s:
        #         return True
        #     else:
        #         s.add(curr)
        # return False
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        
        #Jan 9
        # return len(set(nums)) != len(nums)
        set_nums = set({})
        for num in nums:
            if num in set_nums:
                return True
            else:
                set_nums.add(num)
        return False