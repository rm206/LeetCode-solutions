class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def next_smaller_elt():
            res = [len(arr)] * len(arr)
            stack = []

            for incoming_index, incoming_val in enumerate(arr):
                # if stack empty or incoming greater than top of stack just add to stack
                # if stack not empty and incoming smaller than top => next smaller found => process
                while stack and incoming_val < stack[-1][0]:
                    val, index = stack.pop()
                    res[index] = incoming_index
                    
                stack.append([incoming_val, incoming_index])

            return res

        def prev_smaller_or_equal():
            res = [-1] * len(arr)
            stack = []

            for incoming_index in range(len(arr)-1, -1, -1):
                incoming_val = arr[incoming_index]

                while stack and incoming_val <= stack[-1][0]:
                    val, index = stack.pop()
                    res[index] = incoming_index
                
                stack.append([incoming_val, incoming_index])
            
            return res
        
        nse = next_smaller_elt()
        psee = prev_smaller_or_equal()
        res = 0
        
        for i in range(len(arr)):
            res += arr[i] * (i - psee[i]) * (nse[i] - i)
        
        return res % (10**9 + 7)