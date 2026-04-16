class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        def backtrack(queens,xy_diff,xy_sum):
            p=len(queens)
            if p==n:
                result.append(queens)
                return 
            
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    backtrack(queens+[q],xy_diff+[p-q],xy_sum+[p+q])
            
        backtrack([],[],[])

        return [["." *i +"Q"+"." *(n - i - 1) for i in sol] for sol in result]