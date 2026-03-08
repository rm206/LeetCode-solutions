class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negs, pos = [], []

        for n in nums:
            if n < 0:
                negs.append(n)
            else:
                pos.append(n)
        
        p1, p2 = 0, 0
        turn = 1
        for i in range(len(nums)):
            if turn == 1:
                nums[i] = pos[p1]
                p1 += 1
            else:
                nums[i] = negs[p2]
                p2 += 1
            turn *= -1
        
        return nums