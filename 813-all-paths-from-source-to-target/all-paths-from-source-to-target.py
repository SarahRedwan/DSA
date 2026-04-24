class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        path=[0]

        def dfs(node):
            if node==len(graph)-1:
                res.append(path[:])
                return 
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor)
                path.pop()
        
        dfs(0)
        return res
        