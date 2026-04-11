class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        matrix = {}
        visited = set()
        for i in range(numCourses):
            matrix[i] = []

        for [course, prereq] in prerequisites:
            matrix[course].append(prereq)

        
        def dfs(course):
            if course in visited:
                return False
            if matrix[course] == []:
                return True
            
            visited.add(course)
            for j in range(len(matrix[course])):
                if not dfs(matrix[course][j]):
                    return False

            visited.remove(course)
            matrix[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True