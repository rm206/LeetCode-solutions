class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.pre = []
        
        run_sum = 0
        for i in nums:
            run_sum += i
            self.pre.append(run_sum)
            
    def sumRange(self, left: int, right: int) -> int:
        to_subtract = 0
        
        if left - 1 >= 0:
            to_subtract = self.pre[left - 1]
        
        return self.pre[right] - to_subtract


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)