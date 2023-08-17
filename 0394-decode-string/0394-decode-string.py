class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                # get string in brackets
                st = []
                while stack and stack[-1] != "[":
                    st.append(stack.pop())
                st = st[::-1]
                st = "".join(st)
                # remove opening bracket
                stack.pop()
                # get num
                num = []
                while stack and stack[-1].isnumeric():
                    num.append(stack.pop())
                num = num[::-1]
                num = int("".join(num))
                # replicate string num times and add to stack
                stack.append(num * st)
        return "".join(stack)