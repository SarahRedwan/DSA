from collections import deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        ancestors = [set() for _ in range(n)]
        queue=deque()
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])
                
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return [sorted(list(ans)) for ans in ancestors]
