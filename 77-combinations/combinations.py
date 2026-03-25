class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backtrack(start,comb):
            if len(comb)==k:
                ans.append(comb[:])
                return 
            for nc in range(start,n+1):
                comb.append(nc)
                backtrack(nc+1,comb)
                comb.pop()
            
        backtrack(1,[])
        return ans