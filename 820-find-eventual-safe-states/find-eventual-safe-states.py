class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        graphre=[[] for i in range(n)]
        outdegree=[0]*n
        queue=deque()
        safe=[False]*n


        for n1 in range(n):
            for n2 in graph[n1]:
                graphre[n2].append(n1)
                outdegree[n1]+=1
        
        for node in range(n):
            if outdegree[node]==0:
                queue.append(node)

        while queue:
            node=queue.popleft()
            safe[node]=True


            for neighbor in graphre[node]:
                outdegree[neighbor]-=1

                if outdegree[neighbor]==0:
                    queue.append(neighbor)
                    
        return [i for i in range(n) if safe[i]]


