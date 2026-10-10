class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        def dfs(course, accessed, result):
            if course in completed:
                return True
            if course in accessed:
                return False
            
            accessed.add(course)

            for x in pre_req[course]:
                if not dfs(x, accessed, result):
                    return False
            
            accessed.remove(course)
            result.append(course)
            completed.add(course)
            return True


        pre_req = defaultdict(set)
        for req in prerequisites:
            x, y = req[0], req[1]
            pre_req[x].add(y)
        
        result = []
        completed = set()
        
        for i in range(numCourses):
            if i not in completed:
                if not dfs(i, set(), result):
                    return []

        return result

            