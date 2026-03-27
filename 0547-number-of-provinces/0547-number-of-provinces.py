class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for j, is_connec in enumerate(isConnected[node]):
                if j != node and is_connec == 1 and j not in visited:
                    dfs(j)

        visited = set()
        ctr = 0
        for i in range(len(isConnected)):
            if i not in visited:
                ctr += 1
                dfs(i)
        
        return ctr