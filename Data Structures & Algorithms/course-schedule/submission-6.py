class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = defaultdict(list)

        for course, preq in prerequisites:
            premap[course].append(preq)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if premap[course] == []:
                return True

            visiting.add(course)
            
            for preq in premap[course]:
                if not dfs(preq):
                    return False
            

            visiting.remove(course)
            premap[course] = []

            return True
        
        for courses in range(numCourses):
            if not dfs(courses):
                return False

        return True
        
