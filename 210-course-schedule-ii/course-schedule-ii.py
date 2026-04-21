from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)

        for a,b in prerequisites:
            graph[a].append(b)


        visiting=set()
        visited=set()
        order=[]

        def dfs(course):
            if course in visiting:
                return False
            if course in visited :
                return True
            
            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return order