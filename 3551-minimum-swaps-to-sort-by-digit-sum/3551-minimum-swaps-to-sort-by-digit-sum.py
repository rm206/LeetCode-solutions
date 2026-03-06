class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sum_of_digits(num):
            return sum(list(map(lambda x: int(x), list(str(num)))))
        
        temp = [[sum_of_digits(n), n] for n in nums]
        temp.sort()

        hmap = {nums[i]:i for i in range(len(nums))}

        res = 0
        
        for i in range(len(nums)):
            if nums[i] != temp[i][1]:
                index_to_swap_with = hmap[temp[i][1]]
                nums[i], nums[index_to_swap_with] = nums[index_to_swap_with], nums[i]
                hmap[nums[i]] = i
                hmap[nums[index_to_swap_with]] = index_to_swap_with
                res += 1
        
        return res