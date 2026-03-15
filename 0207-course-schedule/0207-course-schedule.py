class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def build_graph():
            g = {x:[] for x in range(numCourses)}
            for u, v in prerequisites:
                g[u].append(v)
            return g
        
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