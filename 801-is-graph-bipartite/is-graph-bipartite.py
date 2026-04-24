class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1 for _ in range(n)]
        for node in range(n):
            if color[node]==-1:
                color[node]=1
            if not self.dfs(node,graph,color):
                return False
        return True
    def dfs(self,node,graph,color):
        for neighbor in graph[node]:
            if color[neighbor]==-1:
                if color[node]==0:
                    color[neighbor]=1
                else:
                    color[neighbor]=0
                if not self.dfs(neighbor,graph,color):
                    return False
            elif color[neighbor]==color[node]:
                return False
        return True

            