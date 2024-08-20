class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
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
        
        return res % (10**9 + 7)