class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def build_graph():
            g = {x:[] for x in range(numCourses)}
            for u, v in prerequisites:
                g[v].append(u)
            return g
        def indegrees():
            i = {x:0 for x in range(numCourses)}
            for node in graph:
                for neigh in graph[node]:
                    i[neigh] += 1
            return i
        
        graph = build_graph()
        indeg = indegrees()
        q = []
        for node in indeg:
            if indeg[node] == 0:
                q.append(node)
        
        res = []

        while q:
            node = q.pop(0)
            res.append(node)
            for neigh in graph[node]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)
        
        return res if len(res) == numCourses else []