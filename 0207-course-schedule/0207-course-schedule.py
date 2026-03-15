"""
        def has_cycle(node):
            visited.add(node)
            dfs_visited.add(node)

            for neigh in graph[node]:
                if neigh not in visited and has_cycle(neigh):
                    return True
                elif neigh in visited and neigh not in dfs_visited:
                    pass
                elif neigh in visited and neigh in dfs_visited:
                    return True
            
            dfs_visited.remove(node)
            return False

        graph = build_graph()
        visited = set()
        dfs_visited = set()
        for n in range(numCourses):
            if n not in visited and has_cycle(n):
                return False
        
        return True
        """
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def build_graph():
            g = {x:[] for x in range(numCourses)}
            for u, v in prerequisites:
                g[u].append(v)
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
        
        return len(res) == numCourses