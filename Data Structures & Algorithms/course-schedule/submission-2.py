class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = defaultdict(set)
        for req in prerequisites:
            x, y = req[0], req[1]
            pre_req[x].add(y)
        
        def dfs(i, accessed):
            if i in completed:
                return True

            if i in accessed:
                return False
            else:
                accessed.add(i)
            
            for req in pre_req[i]:
                if not dfs(req, accessed):
                    return False
            
            completed.add(i)
            return True
            
        completed = set()
        accessed = set()

        for i in range(numCourses):
            if i in completed:
                continue
            dfs(i, set())
        
        return len(completed) == numCourses
            
            




