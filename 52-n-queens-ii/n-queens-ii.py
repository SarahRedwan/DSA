class Solution:
    def totalNQueens(self, n: int) -> int:
        count=0
        def backtrack(queens,xy_diff,xy_sum):
            nonlocal count
            p=len(queens)

            if p==n:
                count+=1
                return 
            

            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    backtrack(queens+[q],xy_diff+[p-q],xy_sum+[p+q])
        
        backtrack([],[],[])
        return count