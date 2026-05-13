class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)


        def find(n):
            if parent[n]!=n:
                return find(parent[n])
            else:
                return n
        def Union(x,y):
            rootx=find(x)
            rooty=find(y)

            if rootx==rooty:
                return False
            

            if rank[rootx]>rank[rooty]:
                parent[rooty]=rootx
                rank[rootx]+=1
            else:
                parent[rootx]=rooty
                rank[rooty]+=1
            return True
        
        for n1,n2 in edges:
            if not Union(n1,n2):
                return [n1,n2]