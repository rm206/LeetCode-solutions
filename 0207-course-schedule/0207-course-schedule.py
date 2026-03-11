class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {x:[] for x in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)
        

        def has_cycle(node):
            visited.add(node)
            dfs_visited.add(node)

            for neigh in graph[node]:
                if neigh in visited and neigh in dfs_visited:
                    return True
                if neigh in visited and neigh not in dfs_visited:
                    pass
                if neigh not in visited and has_cycle(neigh):
                    return True
            
            dfs_visited.remove(node)
            return False

        visited = set()
        dfs_visited = set()
        for i in range(numCourses):
            if i not in visited and has_cycle(i):
                return False
        return True