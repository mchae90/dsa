class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        hset = set()

        def dfs(crs):
            # Base case: if course already visited, return False
            if crs in hset:
                return False
            # if there are no prereq for the course return True
            if preMap[crs] == []:
                return True
            hset.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            hset.remove(crs)
            preMap[crs] = []
            return True

        # Must iterate thru numCourses to ensure full coverage
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True