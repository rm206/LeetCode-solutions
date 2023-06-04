#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        def knows(M, p1, p2) -> bool:
            if M[p1][p2] == 1:
                return True
            return False
        
        stack = []
        for i in range(n):
            stack.append(i)
        while len(stack) != 1:
            person1 = stack.pop()
            person2 = stack.pop()
            if knows(M, person1, person2):
                stack.append(person2)
            else:
                stack.append(person1)
        
        potential_candidate = stack.pop()
        # is_celebrity_row = True
        # is_celebrity_col = True
        for i in range(n):
            if M[potential_candidate][i] == 1:
                # is_celebrity_row = False
                return -1
            if potential_candidate != i:
                if M[i][potential_candidate] == 0:
                    # is_celebrity_col = False
                    return -1
        
        # if is_celebrity_row and is_celebrity_col:
        #     return potential_candidate
        # else:
        #     return -1
        return potential_candidate
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends