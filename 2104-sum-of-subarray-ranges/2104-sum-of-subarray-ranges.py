class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def sumSubarrayMins(arr):
            def calc_nse():
                res = [len(arr)] * len(arr)
                stack = []

                for i in range(len(arr)):
                    while stack and arr[stack[-1]] > arr[i]:
                        index = stack.pop()
                        res[index] = i
                    stack.append(i)

                return res
            
            def calc_psee():
                res = [-1] * len(arr)
                stack = []

                for i in range(len(arr)):
                    if not stack:
                        stack.append(i)
                    else:
                        while stack and arr[stack[-1]] > arr[i]:
                            stack.pop()
                        res[i] = stack[-1] if stack else -1
                        stack.append(i)
                
                return res

            nse = calc_nse() 
            prev_eq_or_smaller = calc_psee()    
            
            res = 0
            for i in range(len(arr)):
                left = i - prev_eq_or_smaller[i]
                right = nse[i] - i

                res += left * right * arr[i]
            
            return res
        
        def sumSubarrayMaxes(arr):
            def calc_nge():
                res = [len(arr)] * len(arr)
                stack = []

                for i in range(len(arr)):
                    while stack and arr[stack[-1]] <= arr[i]:
                        index = stack.pop()
                        res[index] = i
                    stack.append(i)

                return res
            
            def calc_pgee():
                res = [-1] * len(arr)
                stack = []

                for i in range(len(arr)):
                    if not stack:
                        stack.append(i)
                    else:
                        while stack and arr[stack[-1]] <= arr[i]:
                            stack.pop()
                        res[i] = stack[-1] if stack else -1
                        stack.append(i)
                
                return res

            nge = calc_nge() 
            prev_eq_or_greater = calc_pgee()    
            
            res = 0
            for i in range(len(arr)):
                left = i - prev_eq_or_greater[i]
                right = nge[i] - i

                res += left * right * arr[i]
            
            return res
        
        return sumSubarrayMaxes(nums) - sumSubarrayMins(nums)